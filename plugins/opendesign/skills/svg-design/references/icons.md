# Icon Design Reference

## Grid System

**Keyline template (24x24):**
- Live area: 20x20 (centered)
- Padding: 2px on all sides
- Stroke aligns to pixel grid at 24x24

```svg
<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Icon stays within 20x20 centered area -->
  <path d="..." stroke="currentColor" stroke-width="2"/>
</svg>
```

## Stroke Widths by Size

| Canvas | Stroke Width |
|--------|-------------|
| 16x16 | 1.5px |
| 24x24 | 2px |
| 32x32 | 2.5px |
| 48x48 | 3px |

## Style Types

### Outline (default)
- Stroke only
- Fill="none"
- Consistent stroke-width

```svg
<circle cx="12" cy="12" r="9" 
        stroke="currentColor" 
        stroke-width="2" 
        fill="none"/>
```

### Filled
- Solid shapes
- No stroke
- Use for emphasis

```svg
<circle cx="12" cy="12" r="9" fill="currentColor"/>
```

### Two-tone
- Primary and secondary colors
- Use opacity for secondary

```svg
<path d="M12 2L2 22h20L12 2z" fill="currentColor"/>
<path d="M12 6L6 18h12L12 6z" fill="currentColor" opacity="0.5"/>
```

## Common Icons

### Arrow Right
```svg
<path d="M5 12h14M12 5l7 7-7 7" 
      stroke="currentColor" 
      stroke-width="2" 
      stroke-linecap="round" 
      stroke-linejoin="round"/>
```

### Check
```svg
<path d="M5 12l5 5L20 7" 
      stroke="currentColor" 
      stroke-width="2" 
      stroke-linecap="round" 
      stroke-linejoin="round"/>
```

### X / Close
```svg
<path d="M18 6L6 18M6 6l12 12" 
      stroke="currentColor" 
      stroke-width="2" 
      stroke-linecap="round"/>
```

### Search
```svg
<circle cx="11" cy="11" r="8" 
        stroke="currentColor" 
        stroke-width="2"/>
<path d="M21 21l-4.35-4.35" 
      stroke="currentColor" 
      stroke-width="2" 
      stroke-linecap="round"/>
```

## Pixel Perfection

At 24x24, coordinates should land on pixels:
- Center: 12, 12
- Quarter points: 6, 18
- Eighths: 3, 9, 15, 21

**Avoid:**
- 12.5 (between pixels, blurry)
- Odd decimals

## Alignment

**Optical vs Mathematical:**
- Center vertically with visual weight, not math center
- Circles appear smaller than squares - make slightly larger
- Pointy shapes (arrows) need more weight on the point side

## Sets to Maintain

When designing a set:
- Consistent stroke width
- Consistent corner radius
- Consistent visual weight
- All at same canvas size

## Testing

Test icons at:
- 100% (intended size)
- 125% (slightly larger)
- 75% (smaller)
- In context (with text, in buttons)

## Common Mistakes

- Inconsistent stroke widths
- Touching edges (no padding)
- Too detailed at small sizes
- Non-pixel-aligned coordinates
- Ignoring optical weight
