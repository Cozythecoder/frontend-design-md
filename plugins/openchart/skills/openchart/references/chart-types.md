# Chart Types Reference

## When to Use Each Chart

### Line Chart
- Time series data
- Trends over time
- Continuous data

```json
{
  "mark": "line",
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "value", "type": "quantitative"}
  }
}
```

### Bar Chart
- Comparing categories
- Rankings (use horizontal)
- Discrete data

**Vertical:**
```json
{
  "mark": "bar",
  "encoding": {
    "x": {"field": "category", "type": "nominal"},
    "y": {"field": "value", "type": "quantitative"}
  }
}
```

**Horizontal (for rankings):**
```json
{
  "mark": "bar",
  "encoding": {
    "x": {"field": "value", "type": "quantitative"},
    "y": {"field": "category", "type": "nominal", "sort": "-x"}
  }
}
```

### Area Chart
- Cumulative totals
- Part-to-whole over time
- Emphasizing volume

```json
{
  "mark": "area",
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "value", "type": "quantitative"}
  }
}
```

### Pie/Donut Chart
- Part-to-whole (simple)
- Limited categories (3-5 max)

```json
{
  "mark": "arc",
  "encoding": {
    "theta": {"field": "value", "type": "quantitative"},
    "color": {"field": "category", "type": "nominal"}
  },
  "config": {
    "innerRadius": 60  // Omit for pie
  }
}
```

### Scatter Plot
- Correlation between two variables
- Distribution
- Outliers

```json
{
  "mark": "point",
  "encoding": {
    "x": {"field": "x_value", "type": "quantitative"},
    "y": {"field": "y_value", "type": "quantitative"},
    "color": {"field": "category", "type": "nominal"}
  }
}
```

### Table
- Raw data display
- Precise values needed
- Multiple columns

```json
{
  "type": "table",
  "data": [...],
  "columns": [
    {"field": "name", "title": "Name"},
    {"field": "value", "title": "Value", "format": ".2f"}
  ]
}
```

## Anti-Patterns

- Don't use pie charts with >5 categories
- Don't use line charts for categorical data
- Don't use bar charts for time series (unless discrete periods)
- Avoid 3D charts (use color/size instead)
