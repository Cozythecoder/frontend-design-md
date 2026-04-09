# Quality Gates Reference

## 11 Non-Negotiable Rules

### Rule 1: Color System Validation

**Check:** Color palette follows design system exactly

**Validations:**
- [ ] Primary color mapped correctly
- [ ] Background colors use semantic tokens
- [ ] Text colors meet contrast requirements
- [ ] No arbitrary hex codes outside system
- [ ] Dark/light variants defined

**Auto-fixes:**
- Replace arbitrary colors with nearest design system equivalent
- Generate missing color variants

### Rule 2: Typography Scale Consistency

**Check:** All text uses systematic type scale

**Validations:**
- [ ] Font family matches design system
- [ ] Sizes follow scale (no arbitrary values)
- [ ] Line heights appropriate for size
- [ ] Font weights in approved range
- [ ] No more than 6 distinct sizes in use

**Violations to catch:**
```css
/* BAD - Arbitrary size */
font-size: 17px;

/* GOOD - Systematic */
font-size: var(--text-body);
/* or */
font-size: 16px; /* Part of 4px scale */
```

### Rule 3: Spacing System Adherence

**Check:** Spacing follows base unit and scale

**Validations:**
- [ ] Base unit is 4px or 8px
- [ ] All spacing values divisible by base
- [ ] No arbitrary margin/padding values
- [ ] Section spacing consistent

**Scale validation:**
```python
def validate_spacing(value, base_unit=8):
    """Check if spacing value follows system"""
    if value % base_unit != 0:
        return False, f"{value}px not divisible by {base_unit}px base"
    
    # Check if it's a standard scale value
    standard_scale = [base_unit * (2 ** i) for i in range(6)]
    if value not in standard_scale:
        return False, f"{value}px not in standard scale {standard_scale}"
    
    return True, "Valid"
```

### Rule 4: Component Consistency

**Check:** All components follow design system patterns

**Validations:**
- [ ] Buttons use standard variants (primary, secondary, ghost)
- [ ] Cards have consistent padding/borders
- [ ] Inputs match design system style
- [ ] Navigation follows header pattern

### Rule 5: Touch Target Size

**Check:** All interactive elements >= 44px

**Validations:**
- [ ] Buttons min 44px height
- [ ] Links have adequate padding
- [ ] Form inputs tall enough
- [ ] Icon buttons 44x44px minimum

### Rule 6: Color Contrast (Accessibility)

**Check:** WCAG AA compliance (4.5:1 for text, 3:1 for UI)

**Validations:**
- [ ] Text on background >= 4.5:1
- [ ] Large text (18px+) >= 3:1
- [ ] UI components >= 3:1
- [ ] Focus indicators visible

**Calculation:**
```python
def contrast_ratio(color1, color2):
    """Calculate WCAG contrast ratio"""
    lum1 = relative_luminance(color1)
    lum2 = relative_luminance(color2)
    
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    
    return (lighter + 0.05) / (darker + 0.05)
```

### Rule 7: Reduced Motion Support

**Check:** Respects prefers-reduced-motion

**Validations:**
- [ ] Animations wrapped in media query check
- [ ] Essential motion preserved (subtle fades)
- [ ] Parallax disabled when preferred
- [ ] No auto-playing video/animation

**Required code:**
```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Rule 8: Focus States

**Check:** All interactive elements have visible focus

**Validations:**
- [ ] Buttons have focus ring
- [ ] Links have focus indicator
- [ ] Form inputs show focus
- [ ] Focus color matches design system (usually primary accent)

### Rule 9: Border Radius Consistency

**Check:** Border radius follows system (usually limited set)

**Validations:**
- [ ] Max 3-4 radius values in use
- [ ] Buttons use standard radius
- [ ] Cards use standard radius
- [ ] No arbitrary values

**Typical scale:**
- sm: 4px
- md: 8px
- lg: 12px or 16px
- full: 9999px (pills)

### Rule 10: Shadow System

**Check**: Shadows follow design system elevation levels

**Validations:**
- [ ] Shadows use system values (not arbitrary)
- [ ] Elevation levels consistent (sm, md, lg)
- [ ] Shadow color matches design system (usually black with opacity)

### Rule 11: No Layout Thrashing

**Check:** Animations don't trigger layout

**Validations:**
- [ ] Animations only use transform, opacity
- [ ] No width/height animations
- [ ] No top/left animations
- [ ] No margin/padding animations

**Safe properties:**
```css
/* SAFE */
transform: translateX(100px);
opacity: 0.5;
filter: blur(4px);
clip-path: inset(0 50% 0 0);

/* UNSAFE - Triggers layout */
width: 200px;
height: 200px;
top: 100px;
left: 50px;
margin: 20px;
padding: 16px;
```

## Validation Script

```python
#!/usr/bin/env python3
"""
Quality Gate Validator
Checks all 11 rules and reports violations
"""

import re
import sys
from pathlib import Path

class QualityValidator:
    RULES = [
        'color_system',
        'typography_scale',
        'spacing_system',
        'component_consistency',
        'touch_targets',
        'color_contrast',
        'reduced_motion',
        'focus_states',
        'border_radius',
        'shadow_system',
        'layout_thrashing'
    ]
    
    def __init__(self, project_path):
        self.project = Path(project_path)
        self.violations = []
        self.warnings = []
    
    def validate(self):
        """Run all validation rules"""
        css_files = list(self.project.rglob('*.css'))
        scss_files = list(self.project.rglob('*.scss'))
        all_style_files = css_files + scss_files
        
        for rule in self.RULES:
            method = getattr(self, f'check_{rule}')
            method(all_style_files)
        
        return self.generate_report()
    
    def check_color_system(self, files):
        """Rule 1: Validate color system"""
        arbitrary_colors = []
        
        for file in files:
            content = file.read_text()
            # Find hex codes not using CSS variables
            hex_codes = re.findall(r':\s*(#[a-fA-F0-9]{3,6})[^;]*;', content)
            arbitrary_colors.extend(hex_codes)
        
        if len(set(arbitrary_colors)) > 8:
            self.violations.append(
                f"Rule 1: Too many arbitrary colors ({len(set(arbitrary_colors))}). "
                "Use design system tokens."
            )
    
    def check_typography_scale(self, files):
        """Rule 2: Validate typography"""
        font_sizes = []
        
        for file in files:
            content = file.read_text()
            sizes = re.findall(r'font-size:\s*(\d+)px', content)
            font_sizes.extend(int(s) for s in sizes)
        
        unique_sizes = set(font_sizes)
        if len(unique_sizes) > 8:
            self.violations.append(
                f"Rule 2: Too many font sizes ({len(unique_sizes)}). "
                "Consolidate to systematic scale."
            )
    
    def check_spacing_system(self, files):
        """Rule 3: Validate spacing"""
        spacing_values = []
        
        for file in files:
            content = file.read_text()
            margins = re.findall(r'margin[^:]*:\s*(\d+)px', content)
            paddings = re.findall(r'padding[^:]*:\s*(\d+)px', content)
            spacing_values.extend(int(v) for v in margins + paddings)
        
        # Check divisibility by 4
        non_compliant = [v for v in spacing_values if v % 4 != 0]
        if non_compliant:
            self.warnings.append(
                f"Rule 3: {len(non_compliant)} spacing values not divisible by 4px"
            )
    
    def check_touch_targets(self, files):
        """Rule 5: Validate touch targets"""
        for file in files:
            content = file.read_text()
            # Find small buttons
            small_buttons = re.findall(
                r'\.btn[^\{]*\{[^}]*height:\s*(\d+)px[^}]*\}',
                content
            )
            for height in small_buttons:
                if int(height) < 44:
                    self.violations.append(
                        f"Rule 5: Button height {height}px < 44px minimum"
                    )
    
    def check_layout_thrashing(self, files):
        """Rule 11: Check for layout-triggering animations"""
        unsafe_properties = ['width', 'height', 'top', 'left', 'margin', 'padding']
        
        for file in files:
            content = file.read_text()
            for prop in unsafe_properties:
                if f'transition: {prop}' in content or f'animation.*{prop}' in content:
                    self.violations.append(
                        f"Rule 11: Unsafe animation property '{prop}' found in {file}"
                    )
    
    def generate_report(self):
        """Generate validation report"""
        report = []
        report.append("=" * 60)
        report.append("QUALITY GATE VALIDATION REPORT")
        report.append("=" * 60)
        report.append(f"\nProject: {self.project}")
        report.append(f"Violations: {len(self.violations)}")
        report.append(f"Warnings: {len(self.warnings)}")
        report.append("")
        
        if self.violations:
            report.append("❌ VIOLATIONS (Must Fix):")
            for v in self.violations:
                report.append(f"  • {v}")
            report.append("")
        
        if self.warnings:
            report.append("⚠️  WARNINGS (Should Fix):")
            for w in self.warnings:
                report.append(f"  • {w}")
            report.append("")
        
        if not self.violations:
            report.append("✅ All quality gates passed!")
        
        return '\n'.join(report)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: validate.py <project-path>")
        sys.exit(1)
    
    validator = QualityValidator(sys.argv[1])
    report = validator.validate()
    print(report)
```

## Usage

```bash
# Run validation
python3 validate-quality.py ./my-project

# Exit codes
0 = All passed
1 = Warnings only
2 = Violations found (must fix)
```

## CI/CD Integration

```yaml
# .github/workflows/design-system.yml
name: Design System Validation

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Validate Design System
        run: |
          python3 ~/.claude/skills/design-systems/scripts/validate-quality.py .
```
