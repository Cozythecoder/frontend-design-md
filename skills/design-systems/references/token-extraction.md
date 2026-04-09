# Token Extraction Reference

## Extraction Targets

Extract existing design tokens from project to enable intelligent adaptation.

### Color Extraction

```python
def extract_colors(project_files):
    """
    Extract all color values from CSS, SCSS, Tailwind config
    """
    colors = {
        'hex': [],
        'rgb': [],
        'hsl': [],
        'css_vars': {},
        'tailwind': {},
    }
    
    # Hex colors: #FFF, #FFFFFF, #FFFFFFFF (with alpha)
    hex_pattern = r'#[a-fA-F0-9]{3,8}\b'
    
    # RGB/RGBA: rgb(255, 255, 255), rgba(255, 255, 255, 0.5)
    rgb_pattern = r'rgba?\([^)]+\)'
    
    # HSL/HSLA: hsl(200, 50%, 50%), hsla(200, 50%, 50%, 0.5)
    hsl_pattern = r'hsla?\([^)]+\)'
    
    # CSS custom properties: --color-primary: #3B82F6
    css_var_pattern = r'--([\w-]+)\s*:\s*([^;]+)'
    
    # Tailwind config colors
    tailwind_patterns = [
        r'colors:\s*{([^}]+)}',
        r'"([\w-]+)":\s*"(#[a-fA-F0-9]+)"',
    ]
    
    for file in project_files:
        content = read_file(file)
        
        colors['hex'].extend(re.findall(hex_pattern, content))
        colors['rgb'].extend(re.findall(rgb_pattern, content))
        colors['hsl'].extend(re.findall(hsl_pattern, content))
        
        # Extract CSS variables
        vars_found = re.findall(css_var_pattern, content)
        for var_name, var_value in vars_found:
            if any(c in var_name.lower() for c in ['color', 'bg', 'background', 'text', 'border']):
                colors['css_vars'][var_name] = var_value.strip()
    
    return deduplicate(colors)
```

### Typography Extraction

```python
def extract_typography(project_files):
    """
    Extract font families, sizes, weights, line-heights
    """
    typography = {
        'families': set(),
        'sizes': set(),
        'weights': set(),
        'line_heights': set(),
        'letter_spacing': set(),
    }
    
    patterns = {
        'font_family': r'font-family\s*:\s*([^;]+)',
        'font_size': r'font-size\s*:\s*([^;]+)',
        'font_weight': r'font-weight\s*:\s*([^;]+)',
        'line_height': r'line-height\s*:\s*([^;]+)',
        'letter_spacing': r'letter-spacing\s*:\s*([^;]+)',
    }
    
    for file in project_files:
        content = read_file(file)
        
        for prop, pattern in patterns.items():
            matches = re.findall(pattern, content)
            typography[prop].update(matches)
    
    return typography
```

### Spacing Extraction

```python
def extract_spacing(project_files):
    """
    Extract margin, padding, gap patterns to detect spacing system
    """
    spacing = {
        'margins': [],
        'paddings': [],
        'gaps': [],
        'base_unit': None,
    }
    
    patterns = {
        'margin': r'margin(?:-(?:top|right|bottom|left))?\s*:\s*([^;]+)',
        'padding': r'padding(?:-(?:top|right|bottom|left))?\s*:\s*([^;]+)',
        'gap': r'gap\s*:\s*([^;]+)',
    }
    
    all_values = []
    
    for file in project_files:
        content = read_file(file)
        
        for prop, pattern in patterns.items():
            matches = re.findall(pattern, content)
            spacing[prop].extend(matches)
            
            # Extract numeric values
            for match in matches:
                nums = re.findall(r'(\d+)px', match)
                all_values.extend(int(n) for n in nums)
    
    # Detect base unit (usually GCD of all spacing values)
    if all_values:
        spacing['base_unit'] = math.gcd(*all_values)
    
    return spacing
```

### Component Extraction

```python
def extract_components(project_files):
    """
    Detect existing component patterns (buttons, cards, etc.)
    """
    components = {
        'buttons': [],
        'cards': [],
        'inputs': [],
        'navigation': [],
    }
    
    patterns = {
        'buttons': [
            r'\.btn[\w-]*',
            r'\.button[\w-]*',
            r'\[class\*="btn"\]',
        ],
        'cards': [
            r'\.card[\w-]*',
            r'\.panel[\w-]*',
            r'\.tile[\w-]*',
        ],
        'inputs': [
            r'\.input[\w-]*',
            r'\.form-control',
            r'\.field[\w-]*',
        ],
        'navigation': [
            r'\.nav[\w-]*',
            r'\.navbar',
            r'\.header[\w-]*',
        ],
    }
    
    for file in project_files:
        content = read_file(file)
        
        for component, patterns_list in patterns.items():
            for pattern in patterns_list:
                matches = re.findall(pattern, content)
                components[component].extend(matches)
    
    return {k: list(set(v)) for k, v in components.items()}
```

## Token Classification

After extraction, classify tokens by role:

```python
def classify_tokens(extracted_tokens):
    """
    Classify extracted tokens into semantic roles
    """
    classification = {
        'colors': {
            'background': [],
            'text': [],
            'primary': [],
            'secondary': [],
            'accent': [],
            'border': [],
        },
        'typography': {
            'display': [],
            'heading': [],
            'body': [],
            'caption': [],
        },
        'spacing': {
            'xs': [],
            'sm': [],
            'md': [],
            'lg': [],
            'xl': [],
        }
    }
    
    # Classify colors by usage frequency and luminance
    for color in extracted_tokens['colors']['hex']:
        luminance = calculate_luminance(color)
        
        if luminance > 0.9:
            classification['colors']['background'].append(color)
        elif luminance < 0.1:
            classification['colors']['text'].append(color)
        elif is_vibrant(color):
            classification['colors']['accent'].append(color)
    
    # Classify typography by size
    for size in extracted_tokens['typography']['sizes']:
        px_value = extract_px_value(size)
        
        if px_value >= 48:
            classification['typography']['display'].append(size)
        elif px_value >= 24:
            classification['typography']['heading'].append(size)
        elif px_value >= 14:
            classification['typography']['body'].append(size)
        else:
            classification['typography']['caption'].append(size)
    
    return classification
```

## Token Comparison

Compare extracted tokens against design system:

```python
def compare_tokens(project_tokens, design_system_tokens):
    """
    Calculate similarity between project tokens and design system
    """
    similarities = {
        'color': 0,
        'typography': 0,
        'spacing': 0,
    }
    
    # Color similarity (using color distance)
    for proj_color in project_tokens['colors']['hex']:
        for sys_color in design_system_tokens['colors']:
            distance = color_distance(proj_color, sys_color)
            if distance < 0.1:  # Very similar
                similarities['color'] += 1
    
    # Typography similarity
    proj_fonts = set(project_tokens['typography']['families'])
    sys_fonts = set(design_system_tokens['typography']['families'])
    similarities['typography'] = len(proj_fonts & sys_fonts) / len(proj_fonts | sys_fonts)
    
    # Spacing similarity
    if project_tokens['spacing']['base_unit'] == design_system_tokens['spacing']['base_unit']:
        similarities['spacing'] = 1.0
    else:
        similarities['spacing'] = 0.5  # Partial match
    
    return similarities
```

## Extraction Report Format

```json
{
  "project": "/path/to/project",
  "detected_framework": "React + Tailwind",
  "tokens": {
    "colors": {
      "hex": ["#3B82F6", "#1F2937", "#F3F4F6", "#10B981"],
      "css_vars": {
        "--color-primary": "#3B82F6",
        "--color-text": "#1F2937"
      },
      "semantic_guess": {
        "primary": "#3B82F6",
        "background": "#F3F4F6",
        "text": "#1F2937",
        "success": "#10B981"
      }
    },
    "typography": {
      "families": ["Inter", "system-ui"],
      "sizes": ["14px", "16px", "20px", "24px", "32px", "48px"],
      "base_scale": "8px grid"
    },
    "spacing": {
      "base_unit": 4,
      "scale": [4, 8, 16, 24, 32, 48, 64],
      "pattern": "4px base, doubling"
    },
    "components": {
      "buttons": [".btn-primary", ".btn-secondary", ".btn-ghost"],
      "cards": [".card", ".card-elevated"],
      "detected_library": "Custom + Tailwind"
    }
  },
  "recommendations": [
    "Project uses 4px spacing base - match with design system",
    "Project uses Inter font - compatible with Linear.app system",
    "Project has 4 colors - design system has 8, suggest expansion"
  ]
}
```
