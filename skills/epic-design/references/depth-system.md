# Depth System Reference

## 6-Level Depth Model

Every element must be assigned to one of six depth levels. Each level automatically governs parallax speed, blur, scale, and shadow intensity.

### Depth Hierarchy

| Level | Name | Parallax | Blur | Scale | z-index | Usage |
|-------|------|----------|------|-------|---------|-------|
| 0 | Far Background | 0.10x | 8px | 0.70 | 0 | Full-width backgrounds |
| 1 | Atmospheric | 0.25x | 4px | 0.85 | 1 | Blobs, lens flares |
| 2 | Decoration | 0.50x | 0 | 1.00 | 2 | Geometric accents |
| 3 | Hero | 0.80x | 0 | 1.05 | 3 | Main products/subjects |
| 4 | Interface | 1.00x | 0 | 1.00 | 4 | Text, UI elements |
| 5 | Foreground FX | 1.20x | 0 | 1.10 | 5 | Particles, effects |

### Technical Implementation

**Formula:**
```javascript
element_translateY = scroll_position * depth_factor * -1
```

**CSS Custom Properties:**
```css
:root {
  --depth-0-factor: 0.10;
  --depth-1-factor: 0.25;
  --depth-2-factor: 0.50;
  --depth-3-factor: 0.80;
  --depth-4-factor: 1.00;
  --depth-5-factor: 1.20;
  --scroll-y: 0;
}
```

**JavaScript Update:**
```javascript
window.addEventListener('scroll', () => {
  document.documentElement.style.setProperty('--scroll-y', window.scrollY);
}, { passive: true });
```

**Layer CSS:**
```css
.layer {
  position: absolute;
  will-change: transform;
}

.depth-0 {
  transform: translateY(calc(var(--scroll-y) * var(--depth-0-factor) * -1));
  filter: blur(8px);
  scale: 0.70;
}

.depth-1 {
  transform: translateY(calc(var(--scroll-y) * var(--depth-1-factor) * -1));
  filter: blur(4px);
  scale: 0.85;
  mix-blend-mode: screen; /* Additive glow */
}

.depth-2 {
  transform: translateY(calc(var(--scroll-y) * var(--depth-2-factor) * -1));
  scale: 1.00;
}

.depth-3 {
  transform: translateY(calc(var(--scroll-y) * var(--depth-3-factor) * -1));
  scale: 1.05;
  filter: drop-shadow(0 25px 50px rgba(0,0,0,0.35));
}

.depth-4 {
  transform: translateY(calc(var(--scroll-y) * var(--depth-4-factor) * -1));
  /* No blur - text must be crisp */
}

.depth-5 {
  transform: translateY(calc(var(--scroll-y) * var(--depth-5-factor) * -1));
  scale: 1.10;
  filter: drop-shadow(0 5px 15px rgba(0,0,0,0.50));
}
```

## Asset Specifications by Depth

| Depth | Size | Format | Weight | Blur | Notes |
|-------|------|--------|--------|------|-------|
| 0 | 1920×1080+ | JPG/WebP | 80-150KB | 8px | Low detail acceptable |
| 1 | 600-1000px | PNG | 30-60KB | 4-8px + CSS | Atmospheric glow |
| 2 | 200-400px | PNG | 20-50KB | - | Moderate shadows |
| 3 | 800-1200px | PNG | 50-120KB | - | Transparent, heavy shadow |
| 4 | - | - | - | - | Crisp text, never blur |
| 5 | 32-128px | PNG | 2-10KB | - | High contrast |

## The Rule of One Hero

**Exactly one dominant asset per scene at 50-85vw on Depth 3.**

### Companion Placement

Companions on Depth 2 measure 15-25% of hero size (8-15vw).

**Horizontal Position:**
```css
/* Position relative to hero's edge */
.companion-left {
  left: calc(50% - 40vw - 10vw); /* 50% - half_hero - gap */
}

.companion-right {
  right: calc(50% - 40vw - 10vw);
}
```

**Vertical Placement:**
- Upper shoulder: `top: 35%`
- Mid waist: `top: 55%`
- Lower base: `top: 72%`

**Scroll-Out Behavior:**
Companions scatter outward rather than just fading:
```css
.companion.scroll-out {
  transform: translateX(-50px) scale(0.8);
  opacity: 0;
}
```

## Floating Animations (Anti-Static)

Prevent static visuals with subtle motion:

```css
@keyframes float-y {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

@keyframes float-rotate {
  0%, 100% { transform: rotate(-3deg); }
  50% { transform: rotate(3deg); }
}

@keyframes float-breathe {
  0%, 100% { scale: 1; }
  50% { scale: 1.05; }
}

@keyframes float-orbit {
  0% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(10px, -10px) rotate(90deg); }
  50% { transform: translate(0, -15px) rotate(180deg); }
  75% { transform: translate(-10px, -10px) rotate(270deg); }
  100% { transform: translate(0, 0) rotate(360deg); }
}
```

**Duration by Depth:**
- Depth 2: 10 seconds
- Depth 3: 8 seconds
- Depth 5: 6 seconds
- Glow layers: 12 seconds

## Glow Layer

Absolutely positioned radial gradients for atmospheric lighting:

```css
.glow-layer {
  position: absolute;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(99,102,241,0.45) 0%, transparent 70%);
  filter: blur(80px);
  animation: float-breathe 12s ease-in-out infinite;
}
```

## Markup Structure

```html
<section class="scene">
  <div class="scene-inner">
    <!-- Depth 0: Far Background -->
    <div class="layer depth-0" aria-hidden="true">
      <img src="background.jpg" alt="">
    </div>
    
    <!-- Depth 1: Atmospheric -->
    <div class="layer depth-1" aria-hidden="true">
      <div class="glow-blob"></div>
    </div>
    
    <!-- Depth 2: Decoration -->
    <div class="layer depth-2" aria-hidden="true">
      <div class="companion-left">...</div>
      <div class="companion-right">...</div>
    </div>
    
    <!-- Depth 3: Hero -->
    <div class="layer depth-3">
      <img src="hero-product.png" alt="Main product">
    </div>
    
    <!-- Depth 4: Interface -->
    <div class="layer depth-4">
      <h1>Headline</h1>
      <p>Description</p>
      <button>CTA</button>
    </div>
    
    <!-- Depth 5: Foreground FX -->
    <div class="layer depth-5" aria-hidden="true">
      <div class="particle"></div>
    </div>
  </div>
</section>
```

## Shadow Intensity Formula

Shadows increase with proximity:

```css
/* Depth 2 - Far decoration */
filter: drop-shadow(0 10px 20px rgba(0,0,0,0.20));

/* Depth 3 - Hero (primary focus) */
filter: drop-shadow(0 25px 50px rgba(0,0,0,0.35));

/* Depth 5 - Foreground (closest) */
filter: drop-shadow(0 5px 15px rgba(0,0,0,0.50));
```

## Performance Notes

- Use `will-change: transform` on all layers
- Throttle scroll updates with `requestAnimationFrame`
- Depth 0 and 1 benefit from reduced quality (heavy blur anyway)
- Consider lazy-loading Depth 0 backgrounds
