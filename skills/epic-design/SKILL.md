# Epic Design Skill

Build immersive, cinematic 2.5D interactive websites using scroll storytelling, parallax depth, text animations, and premium scroll effects — no WebGL required.

## Trigger Phrases

Use this skill when user says:
- "make it feel alive"
- "Apple-style animation"
- "sections that overlap"
- "product rises between sections"
- "immersive"
- "scrollytelling"
- "scroll-driven visual effect"
- "cinematic website"
- "parallax depth"

## Pre-Development Protocol

**ALWAYS check for `project-context.md` before coding.**

### Step 1: Asset Inspection
Verify image formats, determine background removal necessity ("JUDGE whether the background actually needs removing"), and establish compositional hierarchy:

- **Heroes**: 50-80vw dominant elements
- **Companions**: 15-25% of hero size
- **Accents**: Small decorative elements

Use `inspect-assets.py` to analyze images before starting.

## Depth Architecture

Six-tier layering system governs all layouts. Every element MUST have a depth level assigned:

| Depth | Layer | Parallax | Blur | Scale | z-index | Usage |
|-------|-------|----------|------|-------|---------|-------|
| 0 | Far Background | 0.10x | 8px | 0.70 | 0 | Full-width backgrounds |
| 1 | Atmospheric | 0.25x | 4px | 0.85 | 1 | Blobs, lens flares |
| 2 | Decoration | 0.50x | 0 | 1.00 | 2 | Geometric accents |
| 3 | Hero | 0.80x | 0 | 1.05 | 3 | Main products/subjects |
| 4 | Interface | 1.00x | 0 | 1.00 | 4 | Text, UI elements |
| 5 | Foreground FX | 1.20x | 0 | 1.10 | 5 | Particles, effects |

### Technical Formula
```
element_translateY = scroll_position * depth_factor * -1
```

### CSS Custom Properties
```css
--depth-0-factor: 0.10;
--depth-1-factor: 0.25;
--depth-2-factor: 0.50;
--depth-3-factor: 0.80;
--depth-4-factor: 1.00;
--depth-5-factor: 1.20;
--scroll-y: 0;
```

### Asset Specifications by Depth

| Depth | Size | Format | Weight | Notes |
|-------|------|--------|--------|-------|
| 0 | 1920×1080+ | JPG/WebP | 80-150KB | Low detail OK (heavy blur) |
| 1 | 600-1000px | PNG | 30-60KB | +40-100px blur in CSS |
| 2 | 200-400px | PNG | 20-50KB | Moderate shadows |
| 3 | 800-1200px | PNG | 50-120KB | Transparent, drop-shadow |
| 4 | - | - | - | Crisp text, NEVER blurred |
| 5 | 32-128px | PNG | 2-10KB | High contrast particles |

## The Rule of One Hero

Exactly **one dominant asset per scene** at 50-85vw on Depth 3.

### Companion Placement
- Size: 15-25% of hero (8-15vw)
- Position: Relative to hero's edge using calc()
- Vertical: Upper shoulder (35%), mid waist (55%), lower base (72%)
- Scroll behavior: Scatter outward on exit (don't just fade)

## Animation Patterns

### 9 Core Motion Patterns

**Pattern 1: Multi-Layer Parallax**
- Data attributes map elements to scroll speeds
- Creates 2.5D depth through vertical translation rates

**Pattern 2: Pinned Sections (Window Over Window)**
- `pin: true` with fixed sections
- Internal content animates while page stays
- "Chapter-like feel where the page lives inside it"

**Pattern 3: Stacking Cards**
- Incrementing z-index + sticky positioning
- Buried cards scale down and darken
- New layers slide overhead

**Pattern 4: Scroll-Linked Timeline**
- "One pixel of scroll = one frame of animation"
- Timeline progress maps to scroll position
- Configurable smoothing

**Pattern 5: Clip-Path Reveals**
- GPU-accelerated masking
- Horizontal wipes, circular iris, window-pane

**Pattern 6: Horizontal Scroll Container**
- Vertical scroll drives horizontal panels
- Automatic snapping calculations

**Pattern 7: 3D Perspective Fly-In**
- Content approaches viewer
- Scale + z-axis + blur transitions
- "User appears to fly toward content"

**Pattern 8: Full-Page Snap Sections**
- Observer plugin for scroll direction
- Coordinated exit/entrance animations

**Pattern 9: Impact Physics**
- Elastic easing with bounce
- Micro-rotation shakes on landing
- Simulates weight and collision

### Floating Animations (Anti-Static)

| Animation | Effect | Duration |
|-----------|--------|----------|
| float-y | Vertical drift | Depth 2: 10s, Depth 3: 8s, Depth 5: 6s |
| float-rotate | Gentle rotation | Staggered delays |
| float-breathe | Scale pulsing | 12s for glow layers |
| float-orbit | Elliptical motion | Depth 1-2 |

### Shadow Intensity by Depth

```css
/* Depth 2 */
filter: drop-shadow(0 10px 20px rgba(0,0,0,0.20));

/* Depth 3 */
filter: drop-shadow(0 25px 50px rgba(0,0,0,0.35));

/* Depth 5 */
filter: drop-shadow(0 5px 15px rgba(0,0,0,0.50));
```

## Technical Constraints

### Safe Properties Only
Animate ONLY these (GPU-accelerated):
- `transform`
- `opacity`
- `filter`
- `clip-path`

**NEVER animate**: width, height, top, left, margin, padding (triggers layout)

### Accessibility Requirements
- `prefers-reduced-motion` fallbacks mandatory
- `aria-hidden="true"` for decorative layers
- Respect `pointer: coarse` for mobile (reduce effects)

### Performance Limits
- Max 80 animated elements per viewport
- Use `will-change: transform` sparingly
- Throttle scroll updates via `requestAnimationFrame`

## Markup Structure

```html
<section class="scene">
  <div class="scene-inner">
    <div class="layer depth-0" aria-hidden="true">...</div>
    <div class="layer depth-1" aria-hidden="true">...</div>
    <div class="layer depth-2" aria-hidden="true">...</div>
    <div class="layer depth-3">...</div>  <!-- Hero content -->
    <div class="layer depth-4">...</div>  <!-- Text, UI -->
    <div class="layer depth-5" aria-hidden="true">...</div>
  </div>
</section>
```

## Quality Assurance: 11 Non-Negotiable Rules

1. ✅ Run `inspect-assets.py` before coding
2. ✅ Every element has assigned depth level
3. ✅ Only ONE hero per scene
4. ✅ Transparent PNGs for Depth 3 heroes
5. ✅ Accessibility fallbacks implemented
6. ✅ `prefers-reduced-motion` respected
7. ✅ Max 80 animated elements
8. ✅ No layout-triggering animations
9. ✅ Mobile detection for reduced effects
10. ✅ Lenis/GSAP ScrollTrigger sync
11. ✅ Validate with `validate-layers.js`

## Operational Modes

1. **Build from scratch**: Full cinematic site
2. **Enhance existing**: Add epic effects to current site
3. **Debug**: Fix performance or layering issues

## Technique Selection Guide

| Project Type | Recommended Techniques |
|--------------|----------------------|
| Product landing | Inter-section floating product, hero fly-in |
| Storytelling | Pinned sections, scroll-linked timeline |
| Portfolio | Stacking cards, horizontal scroll |
| App showcase | 3D perspective, clip-path reveals |
| Event/promo | Full-page snap, impact physics |

## References

- [depth-system.md](references/depth-system.md) - Complete 2.5D parallax specification
- [motion-system.md](references/motion-system.md) - GSAP patterns and scroll integration
- [text-animations.md](references/text-animations.md) - Word reveals, scroll lighting
- [directional-reveals.md](references/directional-reveals.md) - Clip-path and masking
- [inter-section-effects.md](references/inter-section-effects.md) - Floating products, overlaps
- [asset-pipeline.md](references/asset-pipeline.md) - Image preparation and sizing
- [performance.md](references/performance.md) - Optimization guidelines
- [accessibility.md](references/accessibility.md) - Reduced motion and ARIA
- [examples.md](references/examples.md) - Real-world implementations

## Scripts

- [inspect-assets.py](scripts/inspect-assets.py) - Analyze images for 2.5D readiness
- [validate-layers.js](scripts/validate-layers.js) - Validate depth layer configuration

---

**Use aggressively for ANY web design task.** Every website you build must feel like a cinematic experience.
