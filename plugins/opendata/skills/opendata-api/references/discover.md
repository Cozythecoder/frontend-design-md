# Discovery Reference

## Natural Language Search

```
GET /v1/discover?q=unemployment rate by state
```

Returns datasets matching query with metadata optimized for LLMs.

## Response Structure

```json
{
  "results": [
    {
      "provider": "bls",
      "dataset": "laus",
      "title": "Local Area Unemployment Statistics",
      "description": "...",
      "columns": [
        {
          "name": "state",
          "type": "string",
          "description": "US state name",
          "sample_values": ["California", "Texas"]
        }
      ],
      "sample_rows": [...],
      "relevance_score": 0.95
    }
  ]
}
```

## Batch Discovery

```
POST /v1/discover/batch
```

Request:
```json
{
  "queries": [
    "GDP by country",
    "inflation rate US",
    "population by city"
  ]
}
```

Response includes deduplicated results across all queries.

## Use Cases

1. **Finding relevant datasets** when user asks vague questions
2. **Exploring available data** in a domain
3. **Discovering related datasets** for joins

## Tips

- Use specific terms: "CPI" not "prices"
- Include geography: "US unemployment" not just "unemployment"
- Include time: "2024" or "historical"
