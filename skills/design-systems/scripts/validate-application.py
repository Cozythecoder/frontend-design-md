#!/usr/bin/env python3
"""
Design System Application Validator
Validates that design system was applied correctly
"""

import sys
import re
from pathlib import Path
from difflib import SequenceMatcher

class DesignSystemValidator:
    """Validates design system application quality"""

    RULES = [
        'color_tokens',
        'typography_scale',
        'spacing_system',
        'component_classes',
        'accessibility',
    ]

    def __init__(self, project_path: str, design_system: str):
        self.project = Path(project_path)
        self.design_system = design_system
        self.violations = []
        self.warnings = []
        self.checks_passed = 0

    def validate(self):
        """Run all validation checks"""
        print(f"🔍 Validating {self.design_system} application...\n")

        self._check_color_tokens()
        self._check_typography_scale()
        self._check_spacing_system()
        self._check_component_classes()
        self._check_accessibility()

        return self._generate_report()

    def _check_color_tokens(self):
        """Check that CSS variables are used"""
        css_files = list(self.project.rglob('*.css')) + list(self.project.rglob('*.scss'))

        has_css_vars = False
        arbitrary_colors = []

        for css_file in css_files[:10]:
            try:
                content = css_file.read_text()

                # Check for CSS variables usage
                if '--color' in content or '--primary' in content:
                    has_css_vars = True

                # Find arbitrary hex codes
                hex_in_properties = re.findall(r':\s*(#[a-fA-F0-9]{3,6})[^;]*;', content)
                arbitrary_colors.extend(hex_in_properties)

            except Exception:
                continue

        if not has_css_vars:
            self.violations.append({
                'rule': 'color_tokens',
                'severity': 'high',
                'message': 'No CSS color variables found',
                'fix': 'Define --color-primary, --color-background, etc.',
            })

        if len(set(arbitrary_colors)) > 5:
            self.warnings.append({
                'rule': 'color_tokens',
                'severity': 'medium',
                'message': f'{len(set(arbitrary_colors))} arbitrary hex colors found',
                'fix': 'Replace with CSS variable references',
            })

        if has_css_vars and len(set(arbitrary_colors)) <= 5:
            self.checks_passed += 1

    def _check_typography_scale(self):
        """Check typography follows systematic scale"""
        css_files = list(self.project.rglob('*.css')) + list(self.project.rglob('*.scss'))

        font_sizes = []

        for css_file in css_files[:10]:
            try:
                content = css_file.read_text()
                sizes = re.findall(r'font-size:\s*(\d+)px', content)
                font_sizes.extend(int(s) for s in sizes)
            except Exception:
                continue

        unique_sizes = set(font_sizes)

        if len(unique_sizes) > 8:
            self.warnings.append({
                'rule': 'typography_scale',
                'severity': 'medium',
                'message': f'Too many font sizes ({len(unique_sizes)})',
                'fix': 'Consolidate to 6-8 systematic sizes',
            })
        else:
            self.checks_passed += 1

    def _check_spacing_system(self):
        """Check spacing follows base unit"""
        css_files = list(self.project.rglob('*.css')) + list(self.project.rglob('*.scss'))

        spacing_values = []

        for css_file in css_files[:10]:
            try:
                content = css_file.read_text()
                margins = re.findall(r'margin[^:]*:\s*(\d+)px', content)
                paddings = re.findall(r'padding[^:]*:\s*(\d+)px', content)
                spacing_values.extend(int(v) for v in margins + paddings)
            except Exception:
                continue

        # Check if values are divisible by 4
        if spacing_values:
            non_compliant = [v for v in spacing_values if v % 4 != 0]
            if len(non_compliant) > len(spacing_values) * 0.2:  # More than 20%
                self.warnings.append({
                    'rule': 'spacing_system',
                    'severity': 'low',
                    'message': f'{len(non_compliant)} spacing values not on 4px grid',
                    'fix': 'Adjust to 4px or 8px base unit',
                })
            else:
                self.checks_passed += 1

    def _check_component_classes(self):
        """Check component classes follow conventions"""
        html_files = list(self.project.rglob('*.html'))
        jsx_files = list(self.project.rglob('*.jsx')) + list(self.project.rglob('*.tsx'))

        all_files = html_files + jsx_files

        component_indicators = {
            'button': ['btn', 'button'],
            'card': ['card'],
            'input': ['input', 'form-control'],
        }

        found_components = {k: False for k in component_indicators}

        for file in all_files[:20]:
            try:
                content = file.read_text().lower()

                for component, indicators in component_indicators.items():
                    for indicator in indicators:
                        if indicator in content:
                            found_components[component] = True

            except Exception:
                continue

        # Check if any components found
        if not any(found_components.values()):
            self.warnings.append({
                'rule': 'component_classes',
                'severity': 'low',
                'message': 'No standard component classes detected',
                'fix': 'Use .btn, .card, .input classes',
            })
        else:
            self.checks_passed += 1

    def _check_accessibility(self):
        """Check basic accessibility"""
        html_files = list(self.project.rglob('*.html'))

        issues = []

        for file in html_files[:10]:
            try:
                content = file.read_text().lower()

                # Check for alt attributes on images
                img_tags = re.findall(r'<img[^>]*>', content)
                for img in img_tags:
                    if 'alt=' not in img:
                        issues.append('Image without alt attribute')

                # Check for focus styles
                if ':focus' not in content and 'focus-visible' not in content:
                    issues.append('No focus styles detected')

            except Exception:
                continue

        if issues:
            self.warnings.append({
                'rule': 'accessibility',
                'severity': 'medium',
                'message': f'Accessibility issues: {", ".join(set(issues))}',
                'fix': 'Add alt attributes, focus styles, ARIA labels',
            })
        else:
            self.checks_passed += 1

    def _generate_report(self):
        """Generate validation report"""
        total_checks = len(self.RULES)
        passed = self.checks_passed

        report = {
            'summary': {
                'design_system': self.design_system,
                'checks_total': total_checks,
                'checks_passed': passed,
                'success_rate': round(passed / total_checks, 2) if total_checks > 0 else 0,
                'violations': len(self.violations),
                'warnings': len(self.warnings),
            },
            'violations': self.violations,
            'warnings': self.warnings,
        }

        return report

    def print_report(self):
        """Print validation report"""
        report = self._generate_report()
        summary = report['summary']

        print("\n" + "=" * 60)
        print("DESIGN SYSTEM VALIDATION REPORT")
        print("=" * 60)

        print(f"\n📊 Summary:")
        print(f"  Design System: {summary['design_system']}")
        print(f"  Checks Passed: {summary['checks_passed']}/{summary['checks_total']}")
        print(f"  Success Rate: {summary['success_rate'] * 100:.0f}%")

        if report['violations']:
            print(f"\n❌ Violations ({len(report['violations'])}):")
            for v in report['violations']:
                print(f"  • [{v['severity'].upper()}] {v['message']}")
                print(f"    → {v['fix']}")

        if report['warnings']:
            print(f"\n⚠️  Warnings ({len(report['warnings'])}):")
            for w in report['warnings']:
                print(f"  • [{w['severity'].upper()}] {w['message']}")
                print(f"    → {w['fix']}")

        if not report['violations'] and not report['warnings']:
            print("\n✅ All validation checks passed!")

        print("\n" + "=" * 60)

        # Return exit code
        return 0 if summary['success_rate'] >= 0.8 else 1


def main():
    if len(sys.argv) < 3:
        print("Usage: validate-application.py <project-path> <design-system>")
        print("\nExample:")
        print("  validate-application.py ./my-project linear.app")
        sys.exit(1)

    project_path = sys.argv[1]
    design_system = sys.argv[2]

    validator = DesignSystemValidator(project_path, design_system)
    validator.validate()
    exit_code = validator.print_report()

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
