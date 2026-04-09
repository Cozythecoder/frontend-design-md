# SVG Animation Reference

## CSS Animations

### Basic Rotation

```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.icon-spin {
  animation: spin 1s linear infinite;
}
```

### Pulse

```css
@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.1); opacity: 0.8; }
}

.icon-pulse {
  animation: pulse 2s ease-in-out infinite;
}
```

### Bounce

```css
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.icon-bounce {
  animation: bounce 1s ease-in-out infinite;
}
```

## Path Animations

### Draw Line

```css
.path-draw {
  stroke-dasharray: 100;
  stroke-dashoffset: 100;
  animation: draw 2s ease forwards;
}

@keyframes draw {
  to { stroke-dashoffset: 0; }
}
```

### Morph

```javascript
// Using GSAP MorphSVG
gsap.to("#icon", {
  morphSVG: "#icon-hover",
  duration: 0.3,
  ease: "power2.out"
});
```

## GPU Acceleration

Animate these properties for 60fps:
- `transform` (translate, scale, rotate)
- `opacity`

**Avoid:**
- `width`, `height` (triggers layout)
- `top`, `left` (use transform instead)
- `stroke-dasharray` during animation (expensive)

## Reduced Motion

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

## Performance Tips

1. Use `will-change: transform` sparingly
2. Batch animations with `transform`
3. Avoid animating many elements simultaneously
4. Use CSS over JS when possible
5. Test on mobile devices

## Common Patterns

### Loading Spinner

```svg
<svg viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="10" 
          stroke="currentColor" 
          stroke-width="2" 
          fill="none"
          stroke-dasharray="30 60"
          class="spinner"/>
</svg>

<style>
.spinner {
  animation: spin 1s linear infinite;
  transform-origin: center;
}
</style>
```

### Hover Effect

```css
.icon-hover {
  transition: transform 0.2s ease, color 0.2s ease;
}

.icon-hover:hover {
  transform: scale(1.1);
  color: #3B82F6;
}
```
