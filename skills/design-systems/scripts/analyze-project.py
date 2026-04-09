#!/usr/bin/env python3
"""
Project Analyzer for Design System Selection
Detects project type, extracts existing tokens, recommends design system
"""

import sys
import json
import re
from pathlib import Path
from collections import Counter

class ProjectAnalyzer:
    """Analyzes project to recommend optimal design system"""

    CATEGORIES = {
        'saas-landing': {
            'keywords': ['pricing', 'signup', 'features', 'testimonials', 'integration', 'demo'],
            'weight': 2.5,
        },
        'dashboard-app': {
            'keywords': ['dashboard', 'chart', 'widget', 'sidebar', 'analytics', 'metric'],
            'weight': 2.0,
        },
        'e-commerce': {
            'keywords': ['product', 'cart', 'checkout', 'shop', 'buy', 'price'],
            'weight': 2.5,
        },
        'portfolio': {
            'keywords': ['portfolio', 'gallery', 'project', 'creative', 'art', 'work'],
            'weight': 2.0,
        },
        'content-publication': {
            'keywords': ['blog', 'article', 'post', 'newsletter', 'author', 'category'],
            'weight': 2.0,
        },
        'service-business': {
            'keywords': ['service', 'contact', 'process', 'team', 'consulting', 'agency'],
            'weight': 1.8,
        },
        'developer-tool': {
            'keywords': ['api', 'docs', 'documentation', 'cli', 'sdk', 'developer'],
            'weight': 2.0,
        },
    }

    DESIGN_SYSTEMS = {
        'saas-landing': ['linear.app', 'vercel.com', 'supabase.com', 'stripe.com', 'notion.so'],
        'dashboard-app': ['linear.app', 'github.com', 'vercel.com/dashboard'],
        'e-commerce': ['apple.com', 'shopify.com', 'nike.com'],
        'portfolio': ['framer.com', 'webflow.com', 'cargo.site'],
        'content-publication': ['medium.com', 'substack.com', 'stripe.com/blog'],
        'service-business': ['cursor.com', 'intercom.com', 'webflow.com'],
        'developer-tool': ['vercel.com', 'github.com', 'docs.rs'],
    }

    def __init__(self, project_path: str):
        self.project = Path(project_path)
        self.analysis = {
            'category': None,
            'confidence': 0,
            'existing_tokens': {},
            'recommendations': [],
        }

    def analyze(self) -> dict:
        """Run complete project analysis"""
        print(f"🔍 Analyzing project: {self.project}\n")

        # Detect category
        self._detect_category()

        # Extract existing tokens
        self._extract_tokens()

        # Generate recommendations
        self._generate_recommendations()

        return self.analysis

    def _detect_category(self):
        """Detect project category from files and content"""
        scores = {cat: 0 for cat in self.CATEGORIES}
        evidence = {cat: [] for cat in self.CATEGORIES}

        # Check all relevant files
        files_to_check = []
        for ext in ['*.html', '*.jsx', '*.tsx', '*.vue', '*.svelte', '*.css', '*.scss']:
            files_to_check.extend(self.project.rglob(ext))

        # Sample files (limit to avoid slowness)
        sample_files = list(files_to_check)[:50]

        for file_path in sample_files:
            try:
                content = file_path.read_text().lower()

                for category, config in self.CATEGORIES.items():
                    for keyword in config['keywords']:
                        count = content.count(keyword)
                        if count > 0:
                            scores[category] += count * config['weight']
                            evidence[category].append(f"'{keyword}' in {file_path.name}")

            except Exception:
                continue

        # Find best match
        if scores:
            best_category = max(scores.items(), key=lambda x: x[1])
            total_score = sum(scores.values())

            confidence = best_category[1] / total_score if total_score > 0 else 0

            self.analysis['category'] = best_category[0]
            self.analysis['confidence'] = round(confidence, 2)
            self.analysis['evidence'] = evidence[best_category[0]][:10]
            self.analysis['all_scores'] = {k: round(v, 1) for k, v in scores.items()}

    def _extract_tokens(self):
        """Extract existing design tokens from project"""
        tokens = {
            'colors': [],
            'fonts': [],
            'spacing': [],
        }

        css_files = list(self.project.rglob('*.css')) + list(self.project.rglob('*.scss'))

        for css_file in css_files[:20]:
            try:
                content = css_file.read_text()

                # Colors
                hex_colors = re.findall(r'#[a-fA-F0-9]{3,6}\b', content)
                tokens['colors'].extend(hex_colors)

                # Fonts
                fonts = re.findall(r'font-family:\s*([^;]+)', content)
                tokens['fonts'].extend(fonts)

                # Spacing
                spacing = re.findall(r'(?:margin|padding|gap):\s*(\d+)px', content)
                tokens['spacing'].extend(int(s) for s in spacing)

            except Exception:
                continue

        # Deduplicate and summarize
        self.analysis['existing_tokens'] = {
            'colors': list(set(tokens['colors']))[:10],
            'fonts': list(set(tokens['fonts']))[:5],
            'spacing_base': self._detect_spacing_base(tokens['spacing']),
        }

    def _detect_spacing_base(self, spacing_values: list) -> int:
        """Detect spacing base unit from values"""
        if not spacing_values:
            return None

        # Find GCD of all spacing values
        import math
        return math.gcd(*spacing_values)

    def _generate_recommendations(self):
        """Generate design system recommendations"""
        category = self.analysis['category']
        confidence = self.analysis['confidence']

        if not category:
            self.analysis['recommendations'].append({
                'type': 'unclear',
                'message': 'Could not detect project category',
                'action': 'Please specify: SaaS, e-commerce, portfolio, etc.'
            })
            return

        # Get recommended design systems
        recommended_systems = self.DESIGN_SYSTEMS.get(category, [])

        if confidence > 0.6 and recommended_systems:
            self.analysis['recommendations'] = [
                {
                    'type': 'primary',
                    'system': recommended_systems[0],
                    'confidence': confidence,
                    'reason': f"Best match for {category}",
                },
                {
                    'type': 'alternative',
                    'system': recommended_systems[1] if len(recommended_systems) > 1 else None,
                    'reason': 'Alternative style',
                },
            ]
        elif confidence > 0.3:
            self.analysis['recommendations'].append({
                'type': 'suggestion',
                'systems': recommended_systems[:3],
                'message': f'Possible {category} project - choose from these systems',
            })
        else:
            self.analysis['recommendations'].append({
                'type': 'ask',
                'message': 'Unclear project type',
                'action': 'Please describe what you are building',
            })

    def print_report(self):
        """Print analysis report"""
        print("\n" + "=" * 60)
        print("PROJECT ANALYSIS REPORT")
        print("=" * 60)

        print(f"\n📊 Category Detection:")
        print(f"  Primary: {self.analysis['category']}")
        print(f"  Confidence: {self.analysis['confidence'] * 100:.0f}%")

        if self.analysis.get('all_scores'):
            print(f"\n  All scores:")
            for cat, score in sorted(self.analysis['all_scores'].items(), key=lambda x: -x[1]):
                bar = "█" * int(score / 5)
                print(f"    {cat:20} {score:5.1f} {bar}")

        if self.analysis.get('evidence'):
            print(f"\n  Evidence:")
            for ev in self.analysis['evidence'][:5]:
                print(f"    • {ev}")

        print(f"\n🎨 Existing Tokens:")
        tokens = self.analysis['existing_tokens']
        if tokens.get('colors'):
            print(f"  Colors: {', '.join(tokens['colors'][:5])}")
        if tokens.get('fonts'):
            print(f"  Fonts: {', '.join(tokens['fonts'][:3])}")
        if tokens.get('spacing_base'):
            print(f"  Spacing base: {tokens['spacing_base']}px")

        print(f"\n💡 Recommendations:")
        for rec in self.analysis['recommendations']:
            if rec.get('system'):
                print(f"  ✨ {rec['system']} ({rec.get('confidence', 0) * 100:.0f}% match)")
            elif rec.get('systems'):
                print(f"  🤔 Consider: {', '.join(rec['systems'])}")
            else:
                print(f"  ❓ {rec.get('message', '')}")

        print("\n" + "=" * 60)


def main():
    if len(sys.argv) < 2:
        print("Usage: analyze-project.py <project-path>")
        sys.exit(1)

    project_path = sys.argv[1]

    analyzer = ProjectAnalyzer(project_path)
    analysis = analyzer.analyze()
    analyzer.print_report()

    # Save JSON report
    report_path = Path(project_path) / 'project-analysis.json'
    with open(report_path, 'w') as f:
        json.dump(analysis, f, indent=2)

    print(f"\n💾 Full report saved to: {report_path}")


if __name__ == '__main__':
    main()
