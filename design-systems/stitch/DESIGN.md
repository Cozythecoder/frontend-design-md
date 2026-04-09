# Design System Inspiration of Google Stitch

## 1. Visual Theme & Atmosphere

Stitch is Google's AI-native design system — built for interfaces that are generated, manipulated, and experienced through AI. The philosophy is **functional clarity over decorative flourish**: every element serves content selection, natural language interaction, and seamless AI-assisted workflows.

The atmosphere is **clean, modern, and quietly intelligent**. Unlike brand-forward systems that use visual drama, Stitch creates space for content and conversation. The interface recedes; the content and AI interaction take center stage.

**Key Characteristics:**
- **Semantic surfaces**: Backgrounds are roles not just colors — background, surface-container, scrim, each with light/dark variants
- **Content-forward**: Picker components, content libraries, and selection interfaces dominate
- **Quiet intelligence**: No visual noise; AI presence felt through functionality, not branding
- **Google Sans everywhere**: Single type family creates unity; variable font weights handle hierarchy
- **Material Icons**: Consistent iconography from Google's established system
- **Surface-based elevation**: Depth via background layers, not shadows
- **Theme fluidity**: Seamless light/dark transitions via semantic tokens

The design feels like a **conversation container** — a neutral, intelligent space where user intent and AI capability meet.

## 2. Color Palette & Roles

Stitch uses semantic tokens that render different values in light vs dark themes.

### Background Surfaces

| Token | Light Value | Dark Value | Usage |
|-------|-------------|------------|-------|
| Background | `#ffffff` | `#191a1f` | Page canvas, base layer |
| Surface Container | `#f3f4f6` | `#1f2025` | Elevated cards, panels |
| Surface Container Low | `#e5e7eb` | `#191a1f` | Subtle containers |
| Surface Container Lowest | `#d1d5db` | `#131318` | Deepest embedded surfaces |
| Scrim | `rgba(0,0,0,0.4)` | `rgba(0,0,0,0.6)` | Modal backdrops, overlays |

### Primary & Interactive

| Role | Light Value | Dark Value | Usage |
|------|-------------|------------|-------|
| Primary | `#1a73e8` | `#8ab4f8` | Primary actions, CTAs |
| On Primary | `#ffffff` | `#191a1f` | Text on primary backgrounds |
| Primary Container | `#e8f0fe` | `#174ea6` | Selected states, filled chips |
| On Primary Container | `#1967d2` | `#e8f0fe` | Text on primary containers |

### Text Colors

| Role | Light Value | Dark Value | Usage |
|------|-------------|------------|-------|
| On Background | `#1f1f1f` | `#e3e3e8` | Primary text |
| On Surface | `#1f1f1f` | `#e3e3e8` | Text on surface containers |
| On Surface Variant | `#444746` | `#c4c7c5` | Secondary text, metadata |
| Outline | `#747775` | `#8f918d` | Borders, dividers |

### State Colors

| State | Light | Dark | Usage |
|-------|-------|------|-------|
| Error | `#d93025` | `#f28b82` | Error states, destructive actions |
| On Error | `#ffffff` | `#601410` | Text on error backgrounds |
| Success | `#188038` | `#81c995` | Success confirmations |
| Warning | `#f9ab00` | `#fde293` | Warnings, cautions |

## 3. Typography Rules

### Font Family

**Primary**: `Google Sans` (Variable Font)
- **Weights**: 400 (Regular), 500 (Medium), 700 (Bold)
- **Fallbacks**: `Roboto, Arial, sans-serif`
- **Variable axes**: wght (weight), wdth (width)

**Icons**: `Google Material Icons`
- Sharp, rounded, outlined, two-tone variants available

### Hierarchy

| Role | Size | Weight | Line Height | Letter Spacing | Usage |
|------|------|--------|-------------|----------------|-------|
| Display Large | 57px | 400 | 64px | -0.25px | Hero headlines |
| Display Medium | 45px | 400 | 52px | 0px | Major section titles |
| Display Small | 36px | 400 | 44px | 0px | Sub-section heroes |
| Headline Large | 32px | 400 | 40px | 0px | Page titles |
| Headline Medium | 28px | 400 | 36px | 0px | Section headers |
| Headline Small | 24px | 400 | 32px | 0px | Card titles |
| Title Large | 22px | 400 | 28px | 0px | Content titles |
| Title Medium | 16px | 500 | 24px | 0.15px | Labels, nav items |
| Title Small | 14px | 500 | 20px | 0.1px | Small labels |
| Body Large | 16px | 400 | 24px | 0.5px | Primary body text |
| Body Medium | 14px | 400 | 20px | 0.25px | Secondary text |
| Body Small | 12px | 400 | 16px | 0.4px | Captions, metadata |
| Label Large | 14px | 500 | 20px | 0.1px | Button text |
| Label Medium | 12px | 500 | 16px | 0.5px | Small labels, badges |
| Label Small | 11px | 500 | 16px | 0.5px | Tags, micro-labels |

### Typography Principles

1. **Google Sans at all sizes**: One variable font with weight adjustments
2. **Medium weight (500) for emphasis**: Preferred over bold (700)
3. **Positive letter-spacing at small sizes**: For readability
4. **Generous line-heights**: Body text uses 1.5 (24px/16px)
5. **Weight 400 as default**: 500 for labels, 700 reserved for strong emphasis

## 4. Component Stylings

### Picker / Content Library

Stitch's signature component — a content selection interface.

**Container:**
- Background: Surface Container
- Padding: 16px
- Grid: Responsive (1-4 columns)

**Cards:**
- Background: Surface
- Border: 1px solid Outline
- Border Radius: 8px-12px
- Padding: 12px-16px
- Gap: 8px-12px between cards

**Selected State:**
- Background: Primary Container
- Checkmark icon: Primary color

### Modal Dialog

**Scrim:**
- Background: Scrim token (semi-transparent)
- Full viewport coverage

**Container:**
- Background: Surface Container
- Border Radius: 16px-20px
- Padding: 24px
- Max Width: 560px (centered)

### Buttons

**Primary Button**
- Background: Primary
- Text: On Primary
- Padding: 12px 24px
- Border Radius: 8px
- Font: 14px/500
- Hover: Slightly lighter shade
- Active: Scale(0.98)

**Secondary Button**
- Background: Surface Container
- Text: On Surface
- Border: 1px solid Outline
- Padding: 12px 24px
- Border Radius: 8px

**Text Button**
- Background: transparent
- Text: Primary
- Padding: 8px 12px
- Hover: Surface Container background

### Navigation / Header

**Structure:**
- Background: Background
- Height: 56px-64px
- Padding: 0 16px
- Logo: Google Sans wordmark or product icon
- Actions: Text buttons or icons on right
- Optional border: 1px solid Outline at bottom

### Inputs / Search

**Structure:**
- Background: Surface Container Lowest
- Border: 1px solid Outline
- Border Radius: 8px-12px
- Padding: 12px 16px
- Focus: 2px solid Primary outline
- Placeholder: On Surface Variant

### Content Cards

**Structure:**
- Background: Surface
- Border Radius: 8px-12px
- Optional border: 1px solid Outline
- Image: Full-width top, object-fit cover
- Content padding: 16px
- Title: Title Medium (16px/500)
- Meta: Body Small (12px/400), On Surface Variant

## 5. Layout Principles

### Spacing System

**Base Unit**: 4px

| Token | Value | Usage |
|-------|-------|-------|
| Space 1 | 4px | Micro spacing, icon gaps |
| Space 2 | 8px | Tight spacing, inline elements |
| Space 3 | 12px | Standard component padding |
| Space 4 | 16px | Card padding, section gaps |
| Space 6 | 24px | Dialog padding, large gaps |
| Space 8 | 32px | Section padding |
| Space 10 | 40px | Major section breaks |
| Space 12 | 48px | Hero spacing |

### Grid & Containers

**Max Widths:**
- Small: 600px
- Medium: 840px
- Large: 1024px
- XLarge: 1280px

**Responsive Breakpoints:**
- Compact: < 600px (1 column)
- Medium: 600-840px (2 columns)
- Expanded: 840-1200px (3-4 columns)
- Large: > 1200px (4 columns)

**Picker Grid:**
- Compact: 1-2 columns
- Medium+: 2-4 columns
- Gap: 8px (compact) → 12px (expanded)

### Layout Patterns

**Content-First:**
- Full-width content area
- Minimal chrome (header, nav)
- Generous whitespace around content
- Picker dominates viewport

**Modal-Centered:**
- Centered with scrim backdrop
- Max-width constraints
- Touch-friendly spacing

## 6. Depth & Elevation

Stitch uses layered surface colors rather than shadows for elevation.

| Level | Surface Token | Usage |
|-------|---------------|-------|
| Base | Background | Page canvas |
| Low | Surface Container Lowest | Deepest embedded surfaces |
| Container | Surface Container | Cards, panels, pickers |
| Surface | Surface | Elevated cards, selected states |
| Overlay | Scrim | Modal backdrops |

### Focus States

- Outline: 2px solid Primary
- Offset: 2px
- Border radius: Matches element radius
- Transition: 150ms ease

## 7. Do's and Don'ts

### Do

- Use semantic tokens (Background, Surface Container, On Surface) — never hardcoded colors
- Support both light and dark themes in every component
- Use Google Sans exclusively — leverage weights 400/500/700 for hierarchy
- Create semantic containers with picker patterns for content selection
- Implement scrim overlays when showing modals/pickers
- Use Material Icons for consistency
- Respect 44x44px minimum touch targets
- Test with real content — Stitch is content-forward

### Don't

- Introduce custom fonts beyond Google Sans
- Use arbitrary colors — all colors must be semantic tokens
- Ignore theme switching — every component must work in light/dark
- Use heavy shadows — elevation comes from surface colors
- Make the interface louder than content — Stitch recedes, content leads
- Mix icon styles — use Material Icons exclusively
- Use decorative gradients — solid surfaces only

## 8. Responsive Behavior

### Breakpoints

| Name | Width | Behavior |
|------|-------|----------|
| Compact | < 600px | Single column, full-width picker |
| Medium | 600-840px | 2 columns, adjusted spacing |
| Expanded | 840-1200px | 3-4 columns, comfortable spacing |
| Large | > 1200px | 4 columns, maximum content width |

### Picker Responsiveness

- Compact: 1-2 columns, cards stack vertically
- Medium+: 2-4 columns, horizontal layout
- Gap scales: 8px → 12px

### Modal Behavior

- Compact: Full-screen takeover, edge-to-edge
- Medium+: Centered modal with scrim, 560px max-width
- Animation: Fade scrim, scale modal 0.95 → 1

### Dynamic Viewport

- Use `svh` (small viewport height) for full-height sections
- Use `dvh` (dynamic viewport height) for mobile compatibility
- Container queries for component-level responsiveness

## 9. Agent Prompt Guide

### Quick Reference

**Backgrounds:**
- Page: Background (#fff / #191a1f)
- Container: Surface Container (#f3f4f6 / #1f2025)
- Deepest: Surface Container Lowest (#d1d5db / #131318)
- Overlay: Scrim (40-60% black)

**Text:**
- Primary: On Background (#1f1f1f / #e3e3e8)
- Secondary: On Surface Variant (#444746 / #c4c7c5)

**Interactive:**
- Primary: #1a73e8 / #8ab4f8
- Outline: #747775 / #8f918d

### Example Prompts

**Content Picker Grid:**
"Create a 3-column content picker. Container: Surface Container, 16px padding. Cards: Surface background, 1px Outline border, 8px radius, 12px gap. Selected state: Primary Container with checkmark. Titles: 14px/500, metadata: 12px/400 On Surface Variant."

**Modal Dialog:**
"Design a modal with scrim overlay. Container: Surface Container, 20px radius, 24px padding, 560px max-width. Title: 24px/400. Actions: right-aligned text buttons."

**Header:**
"Build a 56px header with Background color. Logo: Google Sans 18px/500. Actions: icon buttons, 44x44px touch targets. Optional 1px Outline border bottom."

**Search Input:**
"Create a search input with Surface Container Lowest background. 1px Outline border, 8px radius, 12px 16px padding. Left search icon in On Surface Variant. Focus: 2px Primary outline."

### Iteration Guide

1. Start with semantic tokens — never hardcode hex values
2. Test both themes — verify light and dark rendering
3. Google Sans only — use weights for hierarchy, not other fonts
4. Content-first spacing — 16px-24px padding around content
5. Surface elevation — use background color changes, not shadows
6. Material Icons — search, close, check, arrow, filter, settings
7. Scrim overlays — always dim background for modals/pickers
8. Touch targets — minimum 44x44px for all interactive elements
