# Filtering Reference

## Basic Filters

```
filter[column]=value
```

Example:
```
filter[year]=2024
filter[country]=United States
```

## Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `eq` | Equal | `filter[status][eq]=active` |
| `neq` | Not equal | `filter[status][neq]=deleted` |
| `gt` | Greater than | `filter[score][gt]=100` |
| `gte` | Greater than or equal | `filter[year][gte]=2020` |
| `lt` | Less than | `filter[price][lt]=50` |
| `lte` | Less than or equal | `filter[age][lte]=65` |
| `in` | In list | `filter[id][in]=1,2,3` |
| `nin` | Not in list | `filter[status][nin]=archived,deleted` |
| `like` | Pattern match | `filter[name][like]=John%` |

## Combining Filters

Multiple filters are ANDed together:

```
filter[year][gte]=2020&filter[year][lte]=2024&filter[country]=USA
```

This returns rows where year is between 2020-2024 AND country is USA.

## Common Pitfalls

- Use `filter[column]`, not bare `column=value`
- URL-encode brackets: `%5B` for `[`, `%5D` for `]`
- Check warnings in response for invalid filters
