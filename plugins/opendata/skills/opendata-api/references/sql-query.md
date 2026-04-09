# SQL Query Reference

## Endpoint

```
POST /v1/datasets/{provider}/{dataset}/query
```

## Request Body

```json
{
  "sql": "SELECT * FROM data WHERE country = ? AND year >= ?",
  "params": ["United States", 2020]
}
```

## Table Names

- Use `data` or `"provider/dataset"` as table name
- Example: `SELECT * FROM data` or `SELECT * FROM "fred/cpi"`

## Allowed Functions

Standard DuckDB SQL with these limitations:
- SELECT only (no INSERT, UPDATE, DELETE)
- No DDL (CREATE, ALTER, DROP)
- No file I/O functions
- 5 second timeout
- 10,000 row limit
- 512MB memory limit

## Common Patterns

**Aggregation:**
```sql
SELECT year, AVG(value) as avg_value
FROM data
GROUP BY year
ORDER BY year
```

**Window functions:**
```sql
SELECT *,
  AVG(value) OVER (PARTITION BY country ORDER BY year) as moving_avg
FROM data
```

**Joins (cross-dataset):**
```sql
SELECT a.*, b.population
FROM data a
JOIN "owid/population" b ON a.country = b.country AND a.year = b.year
```

Use `POST /v1/query` for cross-dataset joins.
