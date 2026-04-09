---
name: openchart
description: Generates OpenChart chart, table, graph, and sankey specs from data, and guides editorial design decisions. Use when visualizing data, selecting chart types, formatting axes, or creating data-driven graphics.
---

# OpenChart Visualization Skill

Write a VizSpec JSON object. The engine validates, compiles, and renders.

## Quick Start

**CSS is required.** Load styles:

```html
<link rel="stylesheet" href="https://esm.sh/@opendata-ai/openchart-vanilla/styles.css">
```

**Render in your framework:**
- React/Vue/Svelte: Use `<Chart>` or `<DataTable>` component
- Vanilla JS: Use `createChart()` function

## Chart Selection Decision Tree

**Temporal x-axis?** → Line chart (time series)

**Categorical + numeric?** → Bar chart
- Rankings: Horizontal bars
- Part-to-whole: Stacked bars
- Distribution: Histogram

**Two numeric variables?** → Scatter plot (correlation)

**Single value to highlight?** → Big number (use `chrome.title`)

**Flow between categories?** → Sankey diagram

**Network relationships?** → Graph visualization

## VizSpec Structure

```json
{
  "mark": "line",
  "data": [...],
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "value", "type": "quantitative"},
    "color": {"field": "series", "type": "nominal"}
  },
  "chrome": {
    "title": "Chart Title",
    "subtitle": "Description of what this shows",
    "source": "Data: FRED Economic Data"
  }
}
```

## Mark Types

| Mark | Type | Use For |
|------|------|---------|
| `line` | Chart | Time series, trends |
| `area` | Chart | Cumulative, part-to-whole |
| `bar` | Chart | Comparison, rankings |
| `arc` | Chart | Pie, donut (use `innerRadius` for donut) |
| `point` | Chart | Scatter, correlation |
| `circle` | Chart | Bubble, sized points |
| `table` | Table | Raw data display |
| `graph` | Graph | Networks, relationships |
| `sankey` | Sankey | Flow, transitions |

**Note:** `column` → use `bar`. `pie`/`donut` → use `arc`. `scatter` → use `point`.

## Bar Orientation

Orientation inferred from encoding:

**Vertical bars:**
```json
{
  "encoding": {
    "x": {"type": "nominal"},  // or "ordinal"
    "y": {"type": "quantitative"}
  }
}
```

**Horizontal bars (rankings):**
```json
{
  "encoding": {
    "x": {"type": "quantitative"},
    "y": {"type": "nominal"}  // or "ordinal"
  }
}
```

## Encoding Channels

| Channel | Description | Common Properties |
|---------|-------------|-------------------|
| `x` | Horizontal position | `field`, `type`, `axis` |
| `y` | Vertical position | `field`, `type`, `axis` |
| `color` | Color coding | `field`, `type`, `scale` |
| `size` | Bubble size, stroke width | `field`, `range` |
| `tooltip` | Hover information | `fields`, `format` |

## Axis Formatting

**Percentages:**
- Data already in percent (0.15 = 15%): `format: ".1f%"`
- Data as decimal (0.15): `format: ".1%"` (multiplies by 100)

**Currency:**
```json
{
  "axis": {
    "format": "$.2f",
    "tickCount": 5
  }
}
```

**Dates:**
```json
{
  "encoding": {
    "x": {
      "field": "date",
      "type": "temporal",
      "axis": {"format": "%b %Y"}
    }
  }
}
```

## Chrome (Container)

```json
{
  "chrome": {
    "title": "Main Title",
    "subtitle": "Context and explanation",
    "source": "Data attribution",
    "footer": "Additional context",
    "download": true  // Enable download button
  }
}
```

## Data Resolution

**Keep under 150 rows per series.**

| Time Span | Recommended Granularity |
|-----------|----------------------|
| < 1 year | Daily or weekly |
| 1-5 years | Weekly or monthly |
| 5-25 years | Monthly or quarterly |
| > 25 years | Yearly |

**Multi-series math:**
3 series × 300 points = 900 data rows. Reduce to 50-80 points per series.

## Common Patterns

### Time Series Line Chart

```json
{
  "mark": "line",
  "data": [{"date": "2024-01", "value": 100}, ...],
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "value", "type": "quantitative"}
  },
  "chrome": {
    "title": "Monthly Trends",
    "source": "Company data"
  }
}
```

### Horizontal Bar (Ranking)

```json
{
  "mark": "bar",
  "data": [{"country": "USA", "gdp": 21000}, ...],
  "encoding": {
    "x": {"field": "gdp", "type": "quantitative", "axis": {"format": "$.0f"}},
    "y": {"field": "country", "type": "nominal", "sort": "-x"}
  }
}
```

### Donut Chart

```json
{
  "mark": "arc",
  "data": [{"category": "A", "value": 30}, ...],
  "encoding": {
    "theta": {"field": "value", "type": "quantitative"},
    "color": {"field": "category", "type": "nominal"}
  },
  "config": {
    "innerRadius": 60  // Donut hole size
  }
}
```

### Multi-Series Line

```json
{
  "mark": "line",
  "data": [
    {"date": "2024-01", "series": "A", "value": 100},
    {"date": "2024-01", "series": "B", "value": 150},
    ...
  ],
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "value", "type": "quantitative"},
    "color": {"field": "series", "type": "nominal"}
  }
}
```

## Anti-Patterns

| Don't | Do Instead |
|-------|-----------|
| `nominal` for numeric fields | Use `quantitative` |
| Forget `encoding.color` for multi-series | Always specify color encoding |
| Bar chart for time series | Use line chart |
| Too many data points | Aggregate, sample, or zoom |
| 3D effects | Use 2D with color/size encoding |
| Dual y-axes | Normalize or use small multiples |

## First Draft Checklist

- [ ] Data resolution appropriate for time span
- [ ] Color encodes the story (not decoration)
- [ ] Y-domain fits data (ceiling 5-10% above max)
- [ ] Axis labels clear and formatted
- [ ] Title explains the takeaway
- [ ] Source attributed

## D3.js Fallback

For cases beyond declarative specs, use custom D3.js:

- [references/d3-core.md](references/d3-core.md) - Core patterns
- [references/d3-animation.md](references/d3-animation.md) - Transitions
- [references/d3-typography.md](references/d3-typography.md) - Text in SVG
- [references/d3-responsive.md](references/d3-responsive.md) - Sizing

## Reference Files

| File | When to Load |
|------|--------------|
| [references/chart-types.md](references/chart-types.md) | Choosing visualization type |
| [references/encoding.md](references/encoding.md) | Axis, scales, formatting |
| [references/data-prep.md](references/data-prep.md) | Transforming data for viz |
| [references/interactive.md](references/interactive.md) | Tooltips, zoom, pan |
| [references/performance.md](references/performance.md) | Large datasets, rendering |
| [references/d3-core.md](references/d3-core.md) | Custom D3.js infographics |
