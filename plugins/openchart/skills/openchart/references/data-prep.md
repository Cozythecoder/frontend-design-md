# Data Preparation Reference

## Data Resolution

Match granularity to time span:

| Time Span | Recommended Granularity |
|-----------|------------------------|
| < 1 year | Daily or weekly |
| 1-5 years | Weekly or monthly |
| 5-25 years | Monthly or quarterly |
| > 25 years | Yearly |

**Rule of thumb:** Keep under 150 rows per series.

## Multi-Series Math

Total rows = series_count × points_per_series

Example:
- 3 series × 300 points = 900 rows (too many)
- 3 series × 50 points = 150 rows (good)

## Data Transformation

### Long to Wide

**Long format (better for charts):**
```json
[
  {"date": "2024-01", "series": "A", "value": 100},
  {"date": "2024-01", "series": "B", "value": 150}
]
```

### Aggregation

Group by time period:
```javascript
data.reduce((acc, row) => {
  const month = row.date.slice(0, 7);
  acc[month] = acc[month] || { date: month, value: 0 };
  acc[month].value += row.value;
  return acc;
}, {})
```

### Normalization

For comparing different scales:
```javascript
const max = Math.max(...data.map(d => d.value));
const normalized = data.map(d => ({
  ...d,
  normalized: d.value / max
}));
```

## Missing Data

**Strategies:**
1. Interpolate (for time series)
2. Show gaps (don't connect lines)
3. Use null/undefined (chart will skip)

## Formatting

**Dates:**
- Use ISO format: "2024-01-15"
- Include timezone if relevant

**Numbers:**
- No commas in raw data
- Store precision, format for display

**Categories:**
- Consistent naming
- No trailing spaces
- Sentence case preferred
