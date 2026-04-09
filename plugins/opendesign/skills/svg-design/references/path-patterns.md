# SVG Path Patterns

## Arc Command

```svg
<path d="M x y A rx ry x-axis-rotation large-arc-flag sweep-flag x y" />
```

**Flags:**
- `large-arc-flag`: 0 = small arc, 1 = large arc
- `sweep-flag`: 0 = counter-clockwise, 1 = clockwise

## Common Shapes

### Rounded Rectangle

```svg
<path d="
  M x y
  h width
  a radius radius 0 0 1 radius radius
  v height
  a radius radius 0 0 1 -radius radius
  h -width
  a radius radius 0 0 1 -radius -radius
  v -height
  a radius radius 0 0 1 radius -radius
  z
"/>
```

### Circle (as path)

```svg
<path d="
  M cx (cy - r)
  A r r 0 1 1 cx (cy + r)
  A r r 0 1 1 cx (cy - r)
  z
"/>
```

### Checkmark

```svg
<path d="M 5 12 L 10 17 L 19 6" 
      fill="none" 
      stroke="currentColor" 
      stroke-width="2" 
      stroke-linecap="round" 
      stroke-linejoin="round"/>
```

### Chevron/Arrow

```svg
<path d="M 9 6 L 15 12 L 9 18" 
      fill="none" 
      stroke="currentColor" 
      stroke-width="2" 
      stroke-linecap="round" 
      stroke-linejoin="round"/>
```

## Fill Rule

For compound shapes with holes:

```svg
<path fill-rule="evenodd" d="..."/>
```

## Optimization

- Use relative commands (lowercase) where possible
- Merge overlapping shapes
- Round coordinates to 2-3 decimal places
