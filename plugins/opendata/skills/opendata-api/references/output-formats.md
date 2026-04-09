# Output Formats Reference

## JSON (default)

```
GET /v1/datasets/fred/cpi?limit=5
```

Returns:
```json
{
  "data": [
    {"date": "2024-01", "value": 308.417},
    ...
  ],
  "meta": {
    "total": 1456,
    "returned": 5
  }
}
```

## CSV

```
GET /v1/datasets/fred/cpi?limit=5&format=csv
```

Returns:
```csv
date,value
2024-01,308.417
...
```

## TSV

```
GET /v1/datasets/fred/cpi?limit=5&format=tsv
```

Tab-separated values.

## XLSX

```
GET /v1/datasets/fred/cpi?limit=1000&format=xlsx
```

Excel format with multiple sheets if applicable.

## Columnar Format

More compact for large datasets:

```
GET /v1/datasets/fred/cpi?response_format=columnar
```

Returns:
```json
{
  "columns": ["date", "value"],
  "data": [
    ["2024-01", 308.417],
    ...
  ]
}
```

## Field Projection

Select specific columns:

```
GET /v1/datasets/fred/cpi?fields=date,value
```

Reduces payload size.

## System Columns

Include metadata:

```
GET /v1/datasets/fred/cpi?include_sources=true
```

Adds:
- `_source_url`: URL of raw data
- `_source_page`: Page number if applicable
- `_ingested_at`: Ingestion timestamp
