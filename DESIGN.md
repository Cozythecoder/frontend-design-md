# Professional Frontend Design System

A comprehensive design specification for modern, visually-rich web experiences with sophisticated depth, imagery, and motion.

---

## 1. Visual Theme & Atmosphere

The design philosophy centers on **layered visual depth with purposeful motion**. The interface feels like a premium physical product — surfaces float at distinct elevations, light behaves realistically across translucent materials, and every transition reinforces spatial relationships. The aesthetic balances professional credibility with approachable warmth.

**Core Design Principles:**
- **Atmospheric depth**: Hero sections use immersive backgrounds (subtle gradients, mesh gradients, or dark cinematic voids) that create immediate visual hierarchy
- **Surface differentiation**: Cards and containers exist at distinct elevation levels with sophisticated shadow stacks
- **Visual rhythm**: Alternating section intensities create breathing room — immersive dark sections followed by clean light content areas
- **Purposeful motion**: Animations guide attention, confirm interactions, and create spatial understanding — never decoration for its own sake
- **Partner credibility**: Third-party logos and integrations are displayed with clarity and respect, using their authentic brand assets

**Key Characteristics:**
- Multi-layer shadow system (4+ layers) creating realistic depth with ambient occlusion
- Strategic glassmorphism on elevated surfaces (modals, floating cards, navigation overlays)
- Gradient backgrounds for hero sections: mesh gradients, aurora effects, or subtle color shifts
- Static icons for feature explanations; partner/tool logos for integrations
- Smooth, physics-based animations with consistent easing curves
- Color temperature shifts between sections (warm parchment → cool professional → dark cinematic)

---

## 2. Color Palette & Roles

### Primary Colors
| Role | Hex | Usage |
|------|-----|-------|
| **Deep Void** | `#0a0a0f` | Dark hero backgrounds, cinematic sections |
| **Pure Black** | `#000000` | Maximum contrast elements, dark mode surfaces |
| **Rich Charcoal** | `#1a1a2e` | Card backgrounds on dark, elevated surfaces |
| **Soft Cream** | `#f5f5f0` | Primary light background — warm neutral |
| **Pure White** | `#ffffff` | Cards on dark backgrounds, maximum elevation |

### Accent Colors
| Role | Hex | Usage |
|------|-----|-------|
| **Electric Indigo** | `#6366f1` | Primary interactive accent, links, focus states |
| **Coral Warmth** | `#f97316` | Secondary accent, CTAs, highlights |
| **Emerald Signal** | `#10b981` | Success states, positive indicators |
| **Rose Alert** | `#f43f5e` | Error states, warnings, destructive actions |

### Gradient System
| Gradient | Definition | Usage |
|----------|------------|-------|
| **Aurora Hero** | `linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%)` | Hero section backgrounds, immersive landing areas |
| **Mesh Dark** | `radial-gradient(ellipse at 20% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 50%), radial-gradient(ellipse at 80% 80%, rgba(249, 115, 22, 0.1) 0%, transparent 50%), #0a0a0f` | Dark hero sections with depth |
| **Soft Elevate** | `linear-gradient(180deg, #ffffff 0%, #f8fafc 100%)` | Light card surfaces, subtle lift |
| **Glass Surface** | `linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%)` | Glassmorphism card backgrounds |

### Header Color Zones
| Zone | Background | Text | Notes |
|------|------------|------|-------|
| **Hero Header** | Transparent or `rgba(10,10,15,0.8)` + blur | White | Overlays hero gradient/image |
| **Content Header** | `#ffffff` or `#f5f5f0` | `#1a1a2e` | Clean, professional |
| **Dark Header** | `#0a0a0f` | `#ffffff` | Cinematic sections |
| **Glass Header** | `rgba(255,255,255,0.8)` + blur | `#1a1a2e` | Floating, modern feel |

### Neutral Scale
| Role | Light Theme | Dark Theme | Usage |
|------|-------------|------------|-------|
| **Text Primary** | `#1a1a2e` | `#ffffff` | Headlines, primary content |
| **Text Secondary** | `#4a5568` | `#a1a1aa` | Descriptions, body text |
| **Text Muted** | `#718096` | `#71717a` | Captions, metadata |
| **Border Subtle** | `#e2e8f0` | `rgba(255,255,255,0.1)` | Dividers, card borders |
| **Border Prominent** | `#cbd5e0` | `rgba(255,255,255,0.2)` | Emphasized boundaries |

---

## 3. Typography Rules

### Font Families
- **Display**: `Inter`, fallback: `system-ui, -apple-system, sans-serif`
- **Body**: `Inter`, same fallback
- **Monospace**: `JetBrains Mono`, fallback: `ui-monospace, SFMono-Regular, Menlo, Monaco`
- **Accent Serif** (optional): `Playfair Display`, for editorial moments

### Hierarchy

| Role | Size | Weight | Line Height | Letter Spacing | Usage |
|------|------|--------|-------------|----------------|-------|
| **Display Hero** | 72px / 4.5rem | 700 | 1.0 | -0.02em | Landing hero, maximum impact |
| **Display Large** | 56px / 3.5rem | 700 | 1.1 | -0.02em | Section heroes |
| **Heading 1** | 48px / 3rem | 700 | 1.1 | -0.02em | Page titles |
| **Heading 2** | 36px / 2.25rem | 600 | 1.2 | -0.01em | Major sections |
| **Heading 3** | 30px / 1.875rem | 600 | 1.2 | -0.01em | Sub-sections |
| **Heading 4** | 24px / 1.5rem | 600 | 1.3 | 0 | Card titles |
| **Heading 5** | 20px / 1.25rem | 600 | 1.4 | 0 | Feature titles |
| **Body Large** | 18px / 1.125rem | 400 | 1.6 | 0 | Lead paragraphs |
| **Body** | 16px / 1rem | 400 | 1.6 | 0 | Standard text |
| **Body Small** | 14px / 0.875rem | 400 | 1.5 | 0 | Descriptions |
| **Caption** | 12px / 0.75rem | 500 | 1.4 | 0.01em | Labels, badges |
| **Overline** | 12px / 0.75rem | 600 | 1.4 | 0.05em | Uppercase labels |

### Typography Principles
- **Negative tracking on display**: Tight letter-spacing (-0.02em) on headings creates visual density and impact
- **Generous line-height on body**: 1.6 line-height for readability, shorter (1.0-1.2) for display
- **Weight hierarchy**: 400 for body, 500 for emphasis, 600 for subheadings, 700 for display
- **Monospace for technical**: JetBrains Mono for code snippets, API references, technical data

---

## 4. Imagery & Visual Assets

### Hero Section Backgrounds

**Gradient Mesh Backgrounds:**
- Use for landing heroes and major section headers
- Subtle animated gradients (CSS-only, GPU-accelerated)
- Colors should complement accent palette without competing
- Implementation: `background: radial-gradient()` layers or mesh gradient images

**Cinematic Dark Backgrounds:**
- Pure void (`#0a0a0f`) with subtle radial glows
- Soft light bloom effects at focal points
- Creates dramatic product/screenshot presentation

**Glass-Over-Image:**
- Background images with heavy overlay (`rgba(0,0,0,0.5)`)
- Frosted glass panels for content containment
- Text always maintains WCAG AA contrast

### Product Screenshots
- **Border treatment**: `1px solid rgba(255,255,255,0.1)` on dark, `#e2e8f0` on light
- **Border radius**: 12px-16px for large screenshots, 8px for inline
- **Shadow**: Multi-layer stack for floating effect (see Depth section)
- **Background**: Screenshots should have consistent internal padding

### Partner/Integration Logos

**When to Use Partner Logos:**
- Trust bar sections ("Used by teams at...")
- Integration directories
- Partnership announcements
- "Works with" feature callouts

**Logo Treatment Rules:**
- **Grayscale by default**: `filter: grayscale(100%)` → `grayscale(0%)` on hover
- **Consistent height**: 24px-40px depending on prominence
- **Opacity**: 60-70% default, 100% on hover
- **Spacing**: 32px-48px between logos minimum
- **Container**: Light logos on dark get subtle border; dark logos on light get subtle background pill

**Static Icons vs Partner Logos:**
| Context | Use |
|---------|-----|
| Explaining a feature | **Static icon** (Lucide/custom) |
| Feature category | **Static icon** |
| Integration partner | **Partner logo** (authentic) |
| Tool/technology used | **Partner logo** if available, else icon |
| Social proof company | **Partner logo** |
| Navigation | **Static icon** |
| Benefit/capability | **Static icon** |

### Illustrations
- **Style**: Clean vector illustrations, subtle depth through layering
- **Color**: Match primary/secondary palette, or complementary accent
- **Usage**: Feature explanations, empty states, onboarding
- **Format**: SVG preferred, animated SVG for interactive moments

---

## 5. Icon System

### Static Icon Usage

**Icon Library**: Lucide Icons (or similar consistent set)

**Color-Coordinated Icon System (Critical)**

Icons must feel integrated into their container's color ecosystem. The unprofessional look (Image 2) happens when:
- Icon colors clash with the card/parent background
- Icons use arbitrary colors unrelated to the heading text
- Icon backgrounds don't harmonize with the overall palette

**The Professional Approach (Image 1):**
| Element | Color Rule |
|---------|------------|
| Icon | Same color as heading text |
| Icon container background | 10-12% opacity tint of the icon color |
| Heading | Matches the icon color |
| Body text | Neutral secondary color |
| Card background | White or neutral surface |

**Color Theme Examples:**
```
Indigo Card:
- Icon: #6366f1 (Electric Indigo)
- Icon background: rgba(99, 102, 241, 0.12)
- Heading: #6366f1
- Body: #4a5568 (neutral)

Coral Card:
- Icon: #f97316 (Coral Warmth)
- Icon background: rgba(249, 115, 22, 0.12)
- Heading: #f97316
- Body: #4a5568 (neutral)

Emerald Card:
- Icon: #10b981 (Emerald Signal)
- Icon background: rgba(16, 185, 129, 0.12)
- Heading: #10b981
- Body: #4a5568 (neutral)
```

**When to Use Icons:**
- Navigation items (accompany text)
- Feature list bullets
- Button adornments (chevrons, arrows)
- Input field indicators
- Status indicators (check, warning, info)
- Feature category headers
- Expand/collapse indicators

**When NOT to Use Icons:**
- Partner/company representation (use their logo)
- Tool/software identification (use authentic logo)
- Brand representation (always use official brand assets)

**Icon Sizing:**
| Context | Size | Notes |
|---------|------|-------|
| Navigation | 20px | Accompanies 14-16px text |
| Inline with text | 16px | Same visual height as text |
| Feature headers | 24px | Matches H5 heading |
| Standalone | 32-40px | Feature callouts |
| Buttons | 16-20px | Internal padding accounted |

**Icon Styling:**
- Stroke width: 1.5px-2px (consistent)
- Color: Must match heading color of the card/container
- Background: 10-12% opacity tint of same color
- Hover: Slight scale (1.05) - NOT color change (maintains ecosystem)

**Anti-Patterns to Avoid:**
- Random icon colors that don't match heading text
- Icon backgrounds that contrast rather than harmonize
- Using the same accent color for ALL icons regardless of context
- Icons that are darker/lighter than their heading text

---

## 6. Component Stylings

### Buttons

**Primary Button**
```
Background: #6366f1 (Electric Indigo)
Text: #ffffff
Padding: 12px 24px
Border-radius: 8px
Font: 16px / 600
Shadow: 0 1px 2px rgba(99, 102, 241, 0.3)
Hover: background #4f46e5, transform translateY(-1px)
Transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1)
```

**Secondary Button**
```
Background: transparent
Border: 1px solid #e2e8f0
Text: #1a1a2e
Padding: 12px 24px
Border-radius: 8px
Hover: background rgba(99, 102, 241, 0.05), border-color #6366f1
```

**Ghost Button**
```
Background: transparent
Text: #6366f1
Padding: 8px 16px
Hover: background rgba(99, 102, 241, 0.1)
```

**Pill Button**
```
Background: #1a1a2e
Text: #ffffff
Border-radius: 9999px
Padding: 10px 20px
Use: Tags, filters, compact actions
```

### Cards

**Standard Card**
```
Background: #ffffff
Border: 1px solid #e2e8f0
Border-radius: 12px
Padding: 24px
Shadow: 0 1px 3px rgba(0, 0, 0, 0.1)
```

**Elevated Card**
```
Background: #ffffff
Border-radius: 16px
Padding: 32px
Shadow: 
  0 1px 2px rgba(0, 0, 0, 0.05),
  0 4px 6px rgba(0, 0, 0, 0.05),
  0 10px 20px rgba(0, 0, 0, 0.08)
Hover: translateY(-2px), shadow intensifies
```

**Glass Card** (Glassmorphism)
```
Background: rgba(255, 255, 255, 0.1)
Backdrop-filter: blur(12px)
Border: 1px solid rgba(255, 255, 255, 0.2)
Border-radius: 16px
Use: Over hero images, floating panels, modals on dark
```

**Feature Card**
```
Background: #ffffff or transparent (on light sections)
Border-radius: 12px
Padding: 24px
Icon: 24-32px, accent color
Title: 20px / 600 / #1a1a2e
Description: 14px / 400 / #4a5568
```

### Navigation

**Transparent Header (Over Hero)**
```
Background: transparent
Position: absolute, top: 0
Links: #ffffff
Logo: White/light variant
CTA: Primary button or white outline
Height: 72px
```

**Solid Header (Content Pages)**
```
Background: #ffffff or #f5f5f0
Border-bottom: 1px solid #e2e8f0
Links: #1a1a2e, 14px / 500
Hover: #6366f1
Height: 64px
Position: sticky, top: 0
```

**Glass Header**
```
Background: rgba(255, 255, 255, 0.8)
Backdrop-filter: blur(12px)
Border-bottom: 1px solid rgba(0, 0, 0, 0.05)
```

### Trust Bar / Logo Grid
```
Container: full-width, padding 48px 0
Background: #f8fafc (subtle contrast)
Logos: grayscale(100%), opacity 0.6
Logo height: 32px
Gap: 48px
Hover on logo: grayscale(0%), opacity 1
```

### Inputs
```
Background: #ffffff
Border: 1px solid #e2e8f0
Border-radius: 8px
Padding: 12px 16px
Font: 16px
Focus: border-color #6366f1, ring 0 0 0 3px rgba(99, 102, 241, 0.1)
Placeholder: #a0aec0
```

---

## 7. Layout Principles

### Spacing System
Base unit: 8px

| Token | Value | Usage |
|-------|-------|-------|
| space-1 | 4px | Micro adjustments |
| space-2 | 8px | Tight component padding |
| space-3 | 12px | Button padding, small gaps |
| space-4 | 16px | Standard gaps, card padding |
| space-5 | 24px | Section internal padding |
| space-6 | 32px | Major component gaps |
| space-7 | 48px | Section padding |
| space-8 | 64px | Large section spacing |
| space-9 | 96px | Hero section padding |
| space-10 | 128px | Major section breaks |

### Section Patterns

**Hero Section (Gradient Background)**
```
Height: min-height 600px, often 100vh
Padding: 96px top (account for nav), 64px bottom
Content: centered or left-aligned, max-width 800px
Background: gradient or image with overlay
Text: white on dark gradient
CTAs: Primary + Secondary, horizontal or stacked
```

**Feature Grid Section**
```
Background: #f5f5f0 (alternates with white)
Padding: 96px 0
Grid: 3 columns desktop, 2 tablet, 1 mobile
Gap: 32px
Cards: Standard or Elevated
```

**Trust/Logos Section**
```
Background: #f8fafc or subtle gradient
Padding: 48px 0
Content: Logo grid, single row or carousel
Text: Optional "Trusted by" label above
```

**Dark Cinematic Section**
```
Background: #0a0a0f or Mesh Dark gradient
Padding: 96px 0
Text: White
Accent: Electric Indigo or Coral
Use: Product showcases, testimonials, CTAs
```

### Container Widths
| Container | Max-Width | Usage |
|-----------|-----------|-------|
| narrow | 640px | Reading content, forms |
| default | 1024px | Standard content |
| wide | 1280px | Feature grids, dashboards |
| full | 100% | Hero sections, full-bleed |

### Grid System
- 12-column implicit grid
- Gap: 24px-32px depending on density
- Responsive breakpoints: 640px, 768px, 1024px, 1280px

---

## 8. Depth & Elevation System

### Shadow Scale

| Level | Shadow Definition | Usage |
|-------|-------------------|-------|
| **Level 0 - Flat** | none | Page background, text content |
| **Level 1 - Subtle** | `0 1px 2px rgba(0,0,0,0.05)` | Cards on light, raised slightly |
| **Level 2 - Raised** | `0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06)` | Interactive cards, buttons |
| **Level 3 - Elevated** | `0 4px 6px rgba(0,0,0,0.05), 0 10px 15px rgba(0,0,0,0.05)` | Dropdowns, popovers |
| **Level 4 - Floating** | `0 10px 25px rgba(0,0,0,0.1), 0 8px 10px rgba(0,0,0,0.04)` | Modals, elevated panels |
| **Level 5 - Prominent** | `0 20px 40px rgba(0,0,0,0.15), 0 10px 20px rgba(0,0,0,0.08)` | Hero images, spotlight elements |

### Glassmorphism Guidelines

**When to Use:**
- Floating cards over hero images/gradients
- Navigation on scroll (glass morphs from transparent)
- Modals and overlays on dark backgrounds
- Dashboard widgets on colorful backgrounds

**Implementation:**
```css
.glass {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
}
```

**Dark Variant:**
```css
.glass-dark {
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}
```

### Z-Index Scale
| Layer | Z-Index | Usage |
|-------|---------|-------|
| Background | -1 | Hero images, decorative |
| Content | 0 | Standard content |
| Raised | 10 | Cards, elevated elements |
| Sticky | 100 | Sticky headers |
| Dropdown | 200 | Dropdown menus |
| Overlay | 300 | Backdrops, scrims |
| Modal | 400 | Modal dialogs |
| Toast | 500 | Notifications |
| Tooltip | 600 | Tooltips |

---

## 9. Animation & Motion

### Animation Principles
- **Purposeful**: Every animation guides or confirms
- **Fast**: Most transitions 150-300ms
- **Smooth**: Easing curves that feel natural
- **Respectful**: Reduced motion media query support

### Easing Functions
| Name | Curve | Usage |
|------|-------|-------|
| **Standard** | `cubic-bezier(0.4, 0, 0.2, 1)` | Most transitions |
| **Enter** | `cubic-bezier(0, 0, 0.2, 1)` | Elements appearing |
| **Exit** | `cubic-bezier(0.4, 0, 1, 1)` | Elements leaving |
| **Bounce** | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Playful emphasis |

### Common Animations

**Button Hover:**
```css
transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
/* On hover: background darkens, translateY(-1px), shadow increases */
```

**Card Hover:**
```css
transition: transform 200ms ease, box-shadow 200ms ease;
/* On hover: translateY(-4px), shadow level increases */
```

**Link Underline:**
```css
transition: background-size 200ms ease;
background-image: linear-gradient(currentColor, currentColor);
background-size: 0% 1px; /* → 100% on hover */
background-position: 0% 100%;
```

**Page Load Stagger:**
```css
/* Children animate in sequence */
animation: fadeInUp 600ms ease-out backwards;
animation-delay: calc(var(--index) * 100ms);
```

**Modal Enter:**
```css
/* Backdrop */
animation: fadeIn 200ms ease-out;
/* Modal */
animation: scaleIn 300ms cubic-bezier(0, 0, 0.2, 1);
```

**Scroll Reveal:**
```css
/* Elements fade in as they enter viewport */
@keyframes reveal {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
```

### Performance Guidelines
- Use `transform` and `opacity` for animations (GPU-accelerated)
- Avoid animating `width`, `height`, `top`, `left`
- Use `will-change` sparingly on elements that will animate
- Support `prefers-reduced-motion`:
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 10. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| sm | <640px | Single column, stacked nav, reduced spacing |
| md | 640-768px | 2-column grids begin |
| lg | 768-1024px | Full nav, 3-column grids |
| xl | 1024-1280px | Maximum content width |
| 2xl | >1280px | Generous margins, expanded layouts |

### Responsive Patterns

**Typography Scaling:**
| Element | Mobile | Desktop |
|---------|--------|---------|
| Display Hero | 40px | 72px |
| Heading 1 | 32px | 48px |
| Heading 2 | 28px | 36px |
| Body | 16px | 16px (consistent) |

**Spacing Scaling:**
- Section padding: 64px mobile → 96px desktop
- Card padding: 20px mobile → 24px desktop
- Grid gaps: 16px mobile → 32px desktop

**Navigation:**
- Desktop: Horizontal links + CTA
- Mobile: Hamburger menu, slide-out drawer

**Hero Sections:**
- Desktop: Side-by-side text/image or centered tall
- Mobile: Stacked, text first, reduced min-height

**Trust Bar:**
- Desktop: Single row, all visible
- Mobile: Horizontal scroll or 2-row grid

---

## 11. Do's and Don'ts

### Do
- Use multi-layer shadow stacks for realistic depth
- Apply glassmorphism sparingly on elevated surfaces over rich backgrounds
- Use partner logos (grayscale, consistent height) for social proof
- Use static icons for features and UI elements
- **Color-coordinate icons** — icon color must match heading text color
- **Tinted icon backgrounds** — use 10-12% opacity of the icon color for the icon container
- Create visual rhythm with alternating section backgrounds
- Use gradient or dark cinematic backgrounds for hero sections
- Animate with purpose — guide attention, confirm interactions
- Ensure text contrast passes WCAG AA on all backgrounds
- Use consistent icon sizing and stroke width
- Apply subtle hover lift (translateY + shadow) on cards

### Don't
- Use heavy drop shadows on flat designs — layer them for realism
- Apply glassmorphism to all surfaces — reserve for special moments
- Mix partner logos with generic icons in the same context
- Use animated/decorative icons for functional UI
- **Mismatched icon colors** — never use icons with colors unrelated to their heading/container
- **Clashing icon backgrounds** — avoid icon backgrounds that don't harmonize with the color palette
- Create hero sections with flat, uninspired backgrounds
- Animate without respecting prefers-reduced-motion
- Use inconsistent logo treatments (color, sizing, opacity)
- Let text get lost on busy gradient backgrounds — use overlays
- Over-animate — avoid animations that don't guide or confirm
- Use shadows darker than rgba(0,0,0,0.2) except for Level 5

---

## 12. Agent Prompt Guide

### Quick Color Reference
- Hero gradient background: Aurora or Mesh Dark
- Content background: `#f5f5f0` (warm) or `#ffffff` (clean)
- Dark cinematic: `#0a0a0f`
- Primary CTA: `#6366f1` (Electric Indigo)
- Secondary CTA: `#f97316` (Coral)
- Text primary: `#1a1a2e`
- Text secondary: `#4a5568`
- Glass surface: `rgba(255,255,255,0.1)` + `blur(12px)`

### Example Component Prompts

**Hero Section with Gradient:**
"Create a hero section with Aurora gradient background (purple-pink-orange). 72px Inter weight 700 headline in white. 18px body text in rgba(255,255,255,0.9). Two CTAs: Primary filled white with dark text, Secondary outline white. Include glass card with product screenshot floating on right. Transparent navigation over hero."

**Feature Card Grid:**
"Design a 3-column feature grid on #f5f5f0 background. Each card: white background, 12px radius, Level 2 shadow, 24px padding. Feature icon 32px in #6366f1. Title 20px weight 600. Description 14px #4a5568. Cards lift 4px on hover with increased shadow."

**Trust Bar:**
"Create a trust bar section with #f8fafc background. 'Trusted by 10,000+ teams' label above. Row of 6 partner logos in grayscale, 32px height, 48px gap, 60% opacity default, 100% on hover."

**Glass Card Over Image:**
"Design a floating glass card: rgba(255,255,255,0.1) background, blur(16px), 1px border rgba(255,255,255,0.2), 16px radius. Content: white text, indigo accent CTA. Position over dark hero background."

**Navigation:**
"Build sticky navigation: transparent initially, becomes glass (blur 12px, rgba(255,255,255,0.9)) on scroll. Logo left, links center, CTA right. Mobile: hamburger with slide-out drawer."

### Iteration Guide
1. Start with color temperature — warm parchment, cool professional, or dark cinematic
2. Define hero background first — it sets the visual tone for the entire page
3. Use shadow levels consistently — cards at Level 2, modals at Level 4
4. Partner logos always grayscale → color on hover, consistent height
5. Icons for features, logos for integrations — never mix them
6. Animation should feel instant but noticeable (150-300ms)
7. Glassmorphism only where there's interesting content behind to blur
8. Typography tracking: tight for display (-0.02em), normal for body
9. Check contrast on gradient backgrounds — use overlays when needed
10. Section rhythm: alternate between immersive (dark/gradient) and content (light)
