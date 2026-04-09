---
name: svg-design
description: Generates and edits SVG logos, icons, and graphics. Use for writing path data, combining shapes, applying transforms, optimizing SVGs, and managing GPU acceleration techniques. Always uses hand-written SVG code like clean markup, never exports from design tools.
---

# SVG Design Skill

SVGs are code. Write them by hand like you'd write any markup: clean, minimal, semantically meaningful.

## Core Principle

**Always include `xmlns` and `viewBox`** in standalone files:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!-- Content -->
</svg>
```

**Default to 24×24** as the industry standard canvas size for icons.

## Task Routing

| Task | Reference |
|------|-----------|
| Arc combinations, arc flags | [path-patterns.md](references/path-patterns.md) |
| Logo techniques, wordmarks | [logos.md](references/logos.md) |
| Icon grids, keyline specs | [icons.md](references/icons.md) |
| Gradients, patterns | [fills.md](references/fills.md) |
| GPU acceleration, motion | [animation.md](references/animation.md) |
| Optimization, compression | [optimization.md](references/optimization.md) |

## Technical Standards

### Canvas Sizes

| Size | Usage |
|------|-------|
| 16×16 | Micro icons, dense UI |
| 24×24 | Default (industry standard) |
| 32×32 | Touch targets, mobile |
| 48×48 | Large display, marketing |

### Styling

**Use `currentColor` for themeability:**

```svg
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <circle cx="12" cy="12" r="10"/>
</svg>
```

**Stroke-width scales with viewBox:**
- 24×24: stroke-width="2"
- 16×16: stroke-width="1.5"
- 48×48: stroke-width="3"

### Shape Primitives vs Paths

**Use primitives when possible** (better readability, easier animation):

```svg
<!-- Good: Primitives -->
<rect x="4" y="4" width="16" height="16" rx="2"/>
<circle cx="12" cy="12" r="10"/>

<!-- Use paths for: complex curves, boolean operations, icons with holes -->
<path d="M12 2L2 22h20L12 2z" fill-rule="evenodd"/>
```

### Rounded Rect to Path Template

```svg
<!-- Rounded rect using arc commands -->
<path d="
  M4 2
  h16
  a2 2 0 0 1 2 2
  v16
  a2 2 0 0 1 -2 2
  h-16
  a2 2 0 0 1 -2 -2
  v-16
  a2 2 0 0 1 2 -2
  z
"/>
```

## Logo Design Protocol

**Always clarify design direction before creating logos.** This step is mandatory for all logo projects.

### Step 1: Present Mood Options

Present curated options via AskUserQuestion:

**Mood:**
- Bold & geometric
- Organic & crafted
- Minimal & typographic
- Playful & dynamic

**Focus:**
- Wordmark (text only)
- Symbol + wordmark
- Symbol only (iconic)

**Inspiration:**
- Domain-specific examples (show 2-3 relevant references)

### Step 2: Explore Metaphors

Create **structural variety** across approaches:

1. **Typographic** — Letterform manipulation, ligatures, custom glyphs
2. **Symbolic** — Abstract mark, pictogram, conceptual representation
3. **Geometric** — Pure shapes, mathematical relationships, grids

Deliver progressively through `variants.js` rather than batch dump.

### Step 3: Refine & Deliver

- Present 2-3 strong directions
- Include dark variants for colored logos
- Convert text to paths for distribution
- Optimize to 2-3 decimal places

## Dark Variants

For colored logos, provide dark-mode versions:

```svg
<!-- Light version -->
<svg class="logo-light" ...>
  <path fill="#6366F1" .../>
</svg>

<!-- Dark version (adjusted colors) -->
<svg class="logo-dark" ...>
  <path fill="#818CF8" .../>  <!-- Lighter variant -->
</svg>
```

## Anti-Patterns

| Don't | Why |
|-------|-----|
| Omit `viewBox` | Breaks scaling |
| Use `px` units | Defeats vector purpose |
| Deeply nested transforms | Hard to debug, performance cost |
| Include editor metadata | Bloats file size |
| Use `<text>` in distributed logos | Font dependency issues |
| Deprecated `xlink:href` | Use `href` instead |
| Export directly from Figma/Illustrator | Bloated, unoptimized code |

## Fill Rule

Use `fill-rule="evenodd"` for compound shapes with holes:

```svg
<path
  fill-rule="evenodd"
  d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z
     M11 7h2v6h-2V7zm0 8h2v2h-2v-2z"
/>
```

## Optimization Checklist

Before finalizing:

- [ ] Convert text to paths (for distribution)
- [ ] Round coordinates to 2-3 decimal places
- [ ] Remove editor metadata
- [ ] Simplify paths (merge overlapping shapes)
- [ ] Minify with SVGO or similar
- [ ] Test at 16×16, 24×24, and 48×48
- [ ] Verify dark variant works

## Reference Files

| File | Content |
|------|---------|
| [references/path-patterns.md](references/path-patterns.md) | Arc commands, bezier curves, boolean operations |
| [references/logos.md](references/logos.md) | Wordmark techniques, symbol design, brand systems |
| [references/icons.md](references/icons.md) | Icon grids, keyline specs, pixel perfection |
| [references/fills.md](references/fills.md) | Gradients, patterns, transparency |
| [references/animation.md](references/animation.md) | GPU acceleration, motion techniques |
| [references/optimization.md](references/optimization.md) | Compression, tooling, best practices |
