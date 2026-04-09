# Pagination and Sort Reference

## Sorting

**Ascending:**
```
sort=year
```

**Descending:**
```
sort=-year
```

**Multiple columns:**
```
sort=country,-year
```

## Pagination

### Offset/Limit

```
limit=100&offset=200
```

Returns rows 201-300.

### Cursor Pagination

For large datasets, use cursor-based pagination:

1. First request:
```
?limit=100
```

2. Get `cursor` from response

3. Next page:
```
?limit=100&cursor=eyJkYXRlIjogIjIwMjQtMDEtMDEifQ==
```

## Sort + Pagination

Always sort before paginating:

```
sort=-date&limit=50&offset=0
```

## Limits

- Default: 100
- Maximum: 1000
- Use smaller limits for better performance

## Performance Tips

- Use cursor pagination for >10,000 rows
- Sort on indexed columns when possible
- Avoid sorting on computed/aggregated columns without group_by
