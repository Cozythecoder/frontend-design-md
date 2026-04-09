# Encoding Reference

## Axis Formatting

### Numbers

```json
{
  "axis": {
    "format": ".0f",
    "tickCount": 5
  }
}
```

Formats:
- `.0f` - Integer (1234)
- `.1f` - One decimal (1234.5)
- `,.0f` - Thousands separator (1,234)
- `.2s` - SI prefix (1.2k)

### Currency

```json
{
  "axis": {
    "format": "$.0f"
  }
}
```

Result: $1,234

### Percentages

Data already percent (0.15):
```json
{
  "axis": {
    "format": ".1f%"
  }
}
```
Result: 15.0%

Data as decimal (0.15):
```json
{
  "axis": {
    "format": ".1%"
  }
}
```
Result: 15.0% (multiplies by 100)

### Dates

```json
{
  "encoding": {
    "x": {
      "field": "date",
      "type": "temporal",
      "axis": {
        "format": "%b %Y"
      }
    }
  }
}
```

Formats:
- `%Y` - 2024
- `%b` - Jan
- `%B` - January
- `%m/%d` - 01/15
- `%Y-%m-%d` - 2024-01-15

## Scales

### Linear (default)

```json
{
  "scale": {
    "type": "linear",
    "domain": [0, 100]
  }
}
```

### Log

```json
{
  "scale": {
    "type": "log",
    "base": 10
  }
}
```

### Ordinal

```json
{
  "scale": {
    "type": "ordinal",
    "domain": ["A", "B", "C"],
    "range": ["#red", "#green", "#blue"]
  }
}
```

## Color Scales

### Categorical

```json
{
  "encoding": {
    "color": {
      "field": "category",
      "type": "nominal",
      "scale": {
        "scheme": "category10"
      }
    }
  }
}
```

Schemes: category10, category20, accent, dark2, paired, set1, set2, set3

### Sequential

```json
{
  "encoding": {
    "color": {
      "field": "value",
      "type": "quantitative",
      "scale": {
        "scheme": "blues"
      }
    }
  }
}
```

Schemes: blues, greens, greys, oranges, purples, reds, viridis, plasma

### Diverging

```json
{
  "encoding": {
    "color": {
      "field": "change",
      "type": "quantitative",
      "scale": {
        "scheme": "rdyg",
        "domain": [-10, 0, 10]
      }
    }
  }
}
```

Schemes: rdgy, rdbu, rdylbu, puor, brbg
