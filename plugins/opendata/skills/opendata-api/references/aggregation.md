# Aggregation Reference

## Aggregate Functions

| Function | Description | Example |
|----------|-------------|---------|
| `count(*)` | Count all rows | `aggregate=count(*)` |
| `count(field)` | Count non-null | `aggregate=count(name)` |
| `sum(field)` | Sum values | `aggregate=sum(sales)` |
| `avg(field)` | Average | `aggregate=avg(score)` |
| `min(field)` | Minimum | `aggregate=min(price)` |
| `max(field)` | Maximum | `aggregate=max(price)` |
| `stddev(field)` | Standard deviation | `aggregate=stddev(value)` |

## Group By

```
GET /v1/datasets/fred/cpi?group_by=year&aggregate=avg(value)
```

## Sorting Aggregates

Sort on computed column names:

```
GET /v1/datasets/owid/gdp?group_by=country&aggregate=sum(gdp)&sort=-sum_gdp&limit=10
```

Note: Use the computed name `sum_gdp` not `sum(gdp)` in sort.

## Multiple Aggregates

Not supported in REST API. Use SQL endpoint for complex aggregations.

## Common Patterns

**Yearly averages:**
```
?group_by=year&aggregate=avg(value)
```

**Count by category:**
```
?group_by=status&aggregate=count(*)
```

**Min/max range:**
```
?aggregate=min(price),max(price)
```
