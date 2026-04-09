# Interactive Features Reference

## Tooltips

Default on hover:

```json
{
  "encoding": {
    "tooltip": {
      "field": "value",
      "type": "quantitative",
      "format": ".2f"
    }
  }
}
```

Multiple fields:

```json
{
  "encoding": {
    "tooltip": [
      {"field": "date", "type": "temporal"},
      {"field": "value", "type": "quantitative", "title": "Amount"},
      {"field": "category", "type": "nominal"}
    ]
  }
}
```

## Legend Interactions

Click legend items to toggle series visibility.

## Zoom and Pan

Enable on scales:

```json
{
  "selection": {
    "grid": {
      "type": "interval",
      "bind": "scales"
    }
  }
}
```

## Brush Selection

Select range:

```json
{
  "selection": {
    "brush": {
      "type": "interval"
    }
  }
}
```

## Click Events

Handle in framework:

```javascript
// React
<Chart 
  onPointClick={(datum) => console.log(datum)}
/>
```

## Performance

For large datasets with interactions:
- Use canvas renderer (default)
- Limit to <10,000 points
- Enable data aggregation
- Use debounced events

## Mobile

Touch interactions:
- Tap for tooltips
- Pinch to zoom
- Pan to scroll
- Ensure 44px minimum touch targets
