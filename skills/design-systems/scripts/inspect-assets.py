#!/usr/bin/env python3
"""
Asset Inspector for Design System Application
Analyzes project assets to determine readiness and requirements
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Tuple
from PIL import Image
import re

class AssetInspector:
    """Inspects project assets for design system compatibility"""

    def __init__(self, project_path: str):
        self.project = Path(project_path)
        self.assets = {
            'images': [],
            'logos': [],
            'icons': [],
            'fonts': [],
        }
        self.report = {
            'summary': {},
            'findings': [],
            'recommendations': [],
        }

    def inspect(self) -> Dict:
        """Run complete asset inspection"""
        print("🔍 Inspecting project assets...\n")

        self._find_all_assets()
        self._analyze_images()
        self._analyze_logos()
        self._analyze_icons()
        self._detect_fonts()
        self._check_brand_assets()

        return self._generate_report()

    def _find_all_assets(self):
        """Find all asset files in project"""
        image_exts = {'.png', '.jpg', '.jpeg', '.webp', '.avif', '.gif', '.svg'}
        font_exts = {'.woff', '.woff2', '.ttf', '.otf'}

        for ext in image_exts:
            self.assets['images'].extend(self.project.rglob(f'*{ext}'))

        for ext in font_exts:
            self.assets['fonts'].extend(self.project.rglob(f'*{ext}'))

        # Look for logo specifically
        logo_patterns = ['logo*', '*logo*', 'brand*', '*brand*', 'favicon*']
        for pattern in logo_patterns:
            for ext in image_exts:
                self.assets['logos'].extend(self.project.rglob(f'{pattern}{ext}'))

        print(f"  📁 Found {len(self.assets['images'])} images")
        print(f"  🎨 Found {len(self.assets['logos'])} logo candidates")
        print(f"  🔤 Found {len(self.assets['fonts'])} font files")

    def _analyze_images(self):
        """Analyze image files for readiness"""
        for img_path in self.assets['images'][:20]:  # Limit to first 20
            try:
                img = Image.open(img_path)
                analysis = self._analyze_single_image(img_path, img)

                if analysis['needs_attention']:
                    self.report['findings'].append({
                        'file': str(img_path),
                        'issues': analysis['issues'],
                        'recommendations': analysis['recommendations']
                    })
            except Exception as e:
                self.report['findings'].append({
                    'file': str(img_path),
                    'issues': [f"Could not analyze: {e}"],
                    'recommendations': ['Check file integrity']
                })

    def _analyze_single_image(self, path: Path, img: Image.Image) -> Dict:
        """Analyze a single image"""
        analysis = {
            'needs_attention': False,
            'issues': [],
            'recommendations': [],
        }

        # Check format
        if img.format == 'JPEG':
            # Check if it needs transparency
            if self._likely_needs_transparency(img):
                analysis['needs_attention'] = True
                analysis['issues'].append('JPEG cannot store transparency')
                analysis['recommendations'].append('Convert to PNG if transparency needed')

        # Check size
        width, height = img.size
        if width > 2000 or height > 2000:
            analysis['needs_attention'] = True
            analysis['issues'].append(f'Oversized: {width}x{height}')
            analysis['recommendations'].append('Resize to max 1200px for web')

        # Check if transparent (for PNGs)
        if img.format == 'PNG' and img.mode in ('RGBA', 'LA', 'PA'):
            has_alpha = any(pixel[3] < 255 for pixel in img.getdata() if len(pixel) > 3)
            if has_alpha:
                analysis['issues'].append('Has transparency (CLEAN)')
            else:
                analysis['issues'].append('No transparency (may need bg removal)')

        return analysis

    def _likely_needs_transparency(self, img: Image.Image) -> bool:
        """Detect if image likely needs transparent background"""
        # Check if it's a product shot (usually needs transparency)
        # Simple heuristic: centered subject, solid background
        width, height = img.size

        # Sample corners and center
        corners = [
            img.getpixel((10, 10)),
            img.getpixel((width-10, 10)),
            img.getpixel((10, height-10)),
            img.getpixel((width-10, height-10)),
        ]
        center = img.getpixel((width//2, height//2))

        # If corners are similar but different from center, likely needs transparency
        corner_avg = tuple(sum(c[i] for c in corners) // 4 for i in range(min(len(c) for c in corners)))

        if len(center) == len(corner_avg):
            diff = sum(abs(center[i] - corner_avg[i]) for i in range(len(center)))
            return diff > 100  # Significant difference

        return False

    def _analyze_logos(self):
        """Analyze logo files"""
        if not self.assets['logos']:
            self.report['recommendations'].append({
                'severity': 'high',
                'message': 'No logo found. Add logo.svg to project root.',
                'action': 'Create or obtain brand logo (SVG preferred)'
            })
            return

        for logo_path in self.assets['logos'][:3]:  # Check top 3 candidates
            try:
                if logo_path.suffix.lower() == '.svg':
                    self.report['summary']['logo_format'] = 'SVG (ideal)'
                    self.report['summary']['logo_path'] = str(logo_path)
                else:
                    self.report['recommendations'].append({
                        'severity': 'medium',
                        'message': f'Logo at {logo_path} is not SVG',
                        'action': 'Convert to SVG for scalability'
                    })
            except Exception:
                pass

    def _analyze_icons(self):
        """Detect icon system"""
        # Check for common icon libraries
        icon_indicators = {
            'lucide': ['lucide', 'lucide-react', 'lucide-vue'],
            'heroicons': ['heroicons', '@heroicons'],
            'fontawesome': ['fontawesome', '@fortawesome'],
            'material': ['material-icons', '@mui/icons'],
        }

        # Check package.json
        package_json = self.project / 'package.json'
        if package_json.exists():
            content = package_json.read_text().lower()
            for icon_set, indicators in icon_indicators.items():
                if any(ind in content for ind in indicators):
                    self.report['summary']['icon_system'] = icon_set
                    break

        if 'icon_system' not in self.report['summary']:
            self.report['recommendations'].append({
                'severity': 'low',
                'message': 'No icon system detected',
                'action': 'Add Lucide Icons (recommended): npm install lucide-react'
            })

    def _detect_fonts(self):
        """Detect font system in use"""
        # Check CSS files for font-family
        css_files = list(self.project.rglob('*.css')) + list(self.project.rglob('*.scss'))

        font_families = set()
        for css_file in css_files[:10]:
            try:
                content = css_file.read_text()
                fonts = re.findall(r'font-family:\s*([^;]+)', content)
                font_families.update(f.strip().strip('"\'') for f in fonts)
            except Exception:
                pass

        if font_families:
            self.report['summary']['detected_fonts'] = list(font_families)[:5]

        # Check for variable fonts
        variable_fonts = [f for f in self.assets['fonts'] if 'var' in f.name.lower()]
        if variable_fonts:
            self.report['summary']['variable_fonts'] = True

    def _check_brand_assets(self):
        """Check for brand color/typography definitions"""
        # Look for tailwind config
        tailwind_config = (
            self.project / 'tailwind.config.js'
            or self.project / 'tailwind.config.ts'
        )

        if tailwind_config.exists():
            content = tailwind_config.read_text()

            # Extract colors if defined
            colors_match = re.search(r'colors:\s*\{([^}]+)\}', content)
            if colors_match:
                self.report['summary']['custom_colors_defined'] = True
            else:
                self.report['recommendations'].append({
                    'severity': 'medium',
                    'message': 'No custom colors in Tailwind config',
                    'action': 'Extend colors with brand palette'
                })

        # Check for CSS variables
        css_vars_found = False
        for css_file in self.project.rglob('*.css'):
            if '--color' in css_file.read_text() or '--primary' in css_file.read_text():
                css_vars_found = True
                break

        self.report['summary']['css_variables'] = css_vars_found

    def _generate_report(self) -> Dict:
        """Generate final inspection report"""
        # Add summary stats
        self.report['summary']['total_images'] = len(self.assets['images'])
        self.report['summary']['total_fonts'] = len(self.assets['fonts'])
        self.report['summary']['critical_issues'] = len([
            r for r in self.report['recommendations']
            if isinstance(r, dict) and r.get('severity') == 'high'
        ])

        # Generate recommendations
        if not self.assets['logos']:
            self.report['recommendations'].append({
                'priority': 1,
                'task': 'Add brand logo',
                'details': 'Create logo.svg in project root'
            })

        if len(self.assets['images']) > 20:
            self.report['recommendations'].append({
                'priority': 2,
                'task': 'Optimize images',
                'details': f'Found {len(self.assets["images"])} images - consider lazy loading'
            })

        return self.report

    def print_report(self):
        """Print human-readable report"""
        print("\n" + "=" * 60)
        print("ASSET INSPECTION REPORT")
        print("=" * 60)

        summary = self.report['summary']
        print(f"\n📊 Summary:")
        print(f"  Images: {summary.get('total_images', 0)}")
        print(f"  Fonts: {summary.get('total_fonts', 0)}")
        print(f"  Logo: {summary.get('logo_format', 'Not found')}")
        print(f"  Icon System: {summary.get('icon_system', 'Not detected')}")

        if self.report['findings']:
            print(f"\n🔍 Findings ({len(self.report['findings'])}):")
            for finding in self.report['findings'][:5]:
                print(f"  • {finding['file']}")
                for issue in finding['issues']:
                    print(f"    - {issue}")

        if self.report['recommendations']:
            print(f"\n💡 Recommendations:")
            for rec in self.report['recommendations']:
                if isinstance(rec, dict):
                    icon = {'high': '❌', 'medium': '⚠️', 'low': '💡'}.get(rec.get('severity'), '•')
                    print(f"  {icon} {rec['message']}")
                    print(f"      → {rec['action']}")
                else:
                    print(f"  • {rec}")

        print("\n" + "=" * 60)


def main():
    if len(sys.argv) < 2:
        print("Usage: inspect-assets.py <project-path>")
        sys.exit(1)

    project_path = sys.argv[1]

    inspector = AssetInspector(project_path)
    report = inspector.inspect()
    inspector.print_report()

    # Save JSON report
    report_path = Path(project_path) / 'asset-inspection.json'
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\n💾 Full report saved to: {report_path}")

    # Exit code based on critical issues
    if report['summary'].get('critical_issues', 0) > 0:
        sys.exit(2)


if __name__ == '__main__':
    main()
