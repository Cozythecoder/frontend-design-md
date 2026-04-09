# Design System Intelligence Skill

Automatically detect project type, analyze intent, and apply the optimal design system from 60+ reference patterns.

## Auto-Detection Triggers

This skill activates when:
- User creates/modifies any web project file (HTML, CSS, JS, JSX, Vue, Svelte)
- User says "design this", "make it look good", "improve UI", "apply design system"
- User mentions specific categories: "landing page", "dashboard", "portfolio", "e-commerce"
- No explicit design system is specified in project

## Phase 1: Project Analysis (Automatic)

**ALWAYS run analysis before selecting design system.**

### Step 1: Detect Project Category

Scan project files to determine type:

```python
# Check for indicators
detections = {
    'saas-landing': ['pricing', 'signup', 'features', 'hero', 'testimonials'],
    'dashboard-app': ['dashboard', 'chart', 'table', 'sidebar', 'widget'],
    'e-commerce': ['product', 'cart', 'checkout', 'shop', 'inventory'],
    'portfolio': ['portfolio', 'gallery', 'project', 'creative', 'art'],
    'content-publication': ['blog', 'article', 'post', 'content', 'newsletter'],
    'brand-showcase': ['brand', 'story', 'about', 'mission', 'values'],
    'developer-tool': ['api', 'docs', 'code', 'terminal', 'github'],
    'service-business': ['service', 'contact', 'process', 'team', 'consulting']
}
```

### Step 2: Analyze Current State

Check existing design tokens:
- Colors in CSS/SCSS/Tailwind config
- Typography (font-family, font-size declarations)
- Spacing (margin, padding, gap patterns)
- Components (button classes, card classes)

### Step 3: Match to Design System Library

Compare against 60+ reference patterns:

| Project Type | Recommended Design Systems |
|--------------|---------------------------|
| **SaaS Landing** | linear.app, vercel.com, supabase.com, stripe.com, notion.so |
| **Dashboard/App** | linear.app (UI), github.com, vercel.com/dashboard, supabase.com/dashboard |
| **E-commerce** | apple.com, shopify.com, nike.com |
| **Portfolio** | framer.com, webflow.com, cargo.site |
| **Content/Blog** | medium.com, substack.com, stripe.com/blog |
| **Developer Tool** | vercel.com, github.com, docs.rs, nextjs.org |
| **Service Business** | cursor.com, intercom.com, webflow.com |
| **Brand/Agency** | tesla.com, apple.com, nike.com |

### Step 4: Confidence Scoring

Calculate match confidence:
```
confidence = (
  category_match * 0.40 +      # Does content match?
  token_similarity * 0.30 +      # Color/typography overlap?
  component_patterns * 0.20 +    # Button/card patterns?
  layout_structure * 0.10        # Grid/flex patterns?
)

If confidence > 0.75: Auto-suggest top match
If 0.50-0.75: Offer 2-3 alternatives
If < 0.50: Ask user for category preference
```

## Phase 2: Pre-Flight Protocol

### Asset Inspection Checklist

**BEFORE applying any design system:**

1. **Check for project-context.md**
   - Does it exist in project root?
   - If no: Create from template with project name, goal, audience

2. **Analyze Current Assets**
   ```bash
   # Run automatically
   python3 ~/.claude/skills/design-systems/scripts/inspect-project.py
   ```
   
   Checks:
   - [ ] Logo exists? (SVG preferred)
   - [ ] Product images? (transparent PNGs for hero?)
   - [ ] Color scheme already defined?
   - [ ] Typography already set?
   - [ ] Existing component library?

3. **Determine Composition Hierarchy**
   - **Hero element**: Largest visual (product shot, illustration, headline)
   - **Supporting elements**: Features, benefits, social proof
   - **Accents**: Decorative elements, patterns

4. **Validate Technical Constraints**
   - [ ] Framework detected (React, Vue, vanilla, etc.)
   - [ ] CSS approach (Tailwind, CSS-in-JS, SCSS, etc.)
   - [ ] Animation capability (GSAP loaded? Framer Motion?)
   - [ ] Performance budget (mobile-first? desktop?)

## Phase 3: Design System Application

### Step 1: Select & Load

Based on analysis, load recommended DESIGN.md:

```
Recommended: Linear.app Design System
Confidence: 87%

Match reasons:
- SaaS landing page detected (pricing, features sections)
- Dark mode preference detected
- Clean typography (Inter-like) found
- Card-based layout patterns present
```

### Step 2: Adapt to Project

**DON'T copy-paste raw.** Adapt based on project analysis:

**Colors:**
- If project has brand colors: Map to design system roles
- If no colors: Use design system palette directly
- Example: "Your blue #3B82F6 → Primary Accent role"

**Typography:**
- If using Inter/System: Keep design system scale
- If using different font: Adapt sizes/weights
- Example: "Roboto instead of Inter → Adjust weights 400→500"

**Spacing:**
- Check existing spacing scale
- Map to design system or preserve if consistent

**Components:**
- Map existing classes to design system patterns
- Example: "Your .btn-primary → design system Primary Button"

### Step 3: Implementation Checklist

Apply design system in priority order:

1. **Foundation** (Critical)
   - [ ] Color CSS variables mapped
   - [ ] Typography scale defined
   - [ ] Spacing system established
   - [ ] Base reset/normalize applied

2. **Layout** (High)
   - [ ] Section spacing (hero, content, footer)
   - [ ] Container widths (max-width, padding)
   - [ ] Grid system (if applicable)

3. **Components** (Medium)
   - [ ] Buttons (primary, secondary, ghost)
   - [ ] Cards (if used)
   - [ ] Forms/inputs (if used)
   - [ ] Navigation (header, footer)

4. **Polish** (Low)
   - [ ] Shadows/elevation
   - [ ] Border radius consistency
   - [ ] Focus states
   - [ ] Hover transitions

## Phase 4: Validation

### Quality Gates

Run after application:

**Visual Consistency Check:**
```python
# Check for violations
violations = []

# 1. Color count
if unique_colors > 8:
    violations.append("Too many colors - simplify palette")

# 2. Typography scale
if font_sizes > 12:
    violations.append("Typography not systematic - consolidate sizes")

# 3. Spacing consistency
if spacing_base not in [4, 8, 16]:
    violations.append("Spacing not following 4/8px grid")

# 4. Touch targets
if touch_targets < 44:
    violations.append("Touch targets below 44px")
```

**Accessibility Check:**
- [ ] Color contrast >= 4.5:1 for text
- [ ] Focus indicators visible
- [ ] Reduced motion respected
- [ ] ARIA labels where needed

**Performance Check:**
- [ ] No layout-thrashing animations
- [ ] Images optimized
- [ ] Fonts subsetted (if custom)

## References

### Design System Analysis
- [category-detection.md](references/category-detection.md) - How to detect project types
- [token-extraction.md](references/token-extraction.md) - Extract existing design tokens
- [matching-algorithm.md](references/matching-algorithm.md) - Confidence scoring logic

### Adaptation Guides
- [color-adaptation.md](references/color-adaptation.md) - Map existing colors to design system
- [typography-adaptation.md](references/typography-adaptation.md) - Font family substitutions
- [spacing-adaptation.md](references/spacing-adaptation.md) - Spacing system mapping
- [component-mapping.md](references/component-mapping.md) - Class name translations

### Validation
- [quality-gates.md](references/quality-gates.md) - 11 non-negotiable rules
- [accessibility-checks.md](references/accessibility-checks.md) - A11y validation
- [performance-checks.md](references/performance-checks.md) - Performance budget

### Category-Specific Patterns
- [saas-landing.md](references/saas-landing.md) - SaaS landing page patterns
- [dashboard-app.md](references/dashboard-app.md) - Dashboard UI patterns
- [e-commerce.md](references/e-commerce.md) - Product/ecommerce patterns
- [portfolio.md](references/portfolio.md) - Creative portfolio patterns
- [content-site.md](references/content-site.md) - Blog/content patterns

## Scripts

- `scripts/analyze-project.py` — Detect category, current tokens
- `scripts/match-design-system.py` — Compare against library
- `scripts/validate-application.py` — Quality gates
- `scripts/generate-adaptation.py` — Map existing to design system
- `scripts/inspect-assets.py` — Check images, logos, brand assets

## Design System Library

60+ systems organized by category in `../design-systems/`:

### SaaS / Developer Tools
- linear.app (dark, Inter, 510 weight)
- vercel.com (Geist, shadow-border)
- supabase.com (warm, postgres-inspired)
- stripe.com (content-rich, gradients)
- notion.so (friendly, rounded)
- github.com (functional, dense)
- cursor.com (editor-focused, syntax colors)

### E-commerce / Product
- apple.com (SF Pro, binary contrast, pill CTAs)
- shopify.com (polarized, Polaris tokens)
- nike.com (bold, dynamic, imagery-first)

### Creative / Portfolio
- framer.com (playful, gradients, bouncy)
- webflow.com (professional, structured)

### Content / Publication
- medium.com (reading-focused, serif body)
- substack.com (warm, newsletter-centric)

### Enterprise
- ibm.com (Carbon design, systematic)
- salesforce.com (functional, dense)

### Automotive / Luxury
- tesla.com (minimal, product-centric)
- ferrari.com (dramatic, red accent)
- bmw.com (technical, precise)

## Usage Flow

```
User: "Build a landing page for my SaaS"
↓
Skill: Analyzes project...
       Detects: SaaS landing intent
       Current state: No design system
↓
Skill: Recommends linear.app (87% match)
       Offers alternatives: vercel.com, stripe.com
↓
User: "Use Linear style"
↓
Skill: Runs pre-flight protocol
       - Creates project-context.md
       - Analyzes assets
       - Checks tech stack
↓
Skill: Applies Linear design system
       - Maps color tokens
       - Sets typography scale
       - Implements components
↓
Skill: Validates output
       - Color contrast check
       - Spacing consistency
       - Quality gate review
↓
Output: Project with Linear-inspired design
```

## Configuration

Override auto-detection by creating `.design-system` in project root:

```json
{
  "system": "linear.app",
  "theme": "dark",
  "adaptations": {
    "primaryColor": "#3B82F6",
    "fontFamily": "Inter"
  }
}
```

---

**This skill merges your 60+ design system collection with epic-style workflow: auto-detection, pre-flight checks, validation, and intelligent adaptation.**
