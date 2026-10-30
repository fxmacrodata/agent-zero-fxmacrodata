### fxmd_risk_sentiment_changes

Recorded risk-sentiment changes

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
  "properties": {
    "after_sequence": {
      "type": "integer",
      "minimum": 0,
      "description": "Optional query parameter. Return changes after this sequence (exclusive).",
      "default": 0,
      "title": "After Sequence"
    },
    "limit": {
      "type": "integer",
      "maximum": 100,
      "minimum": 1,
      "description": "Optional query parameter. Maximum retained changes per page.",
      "default": 20,
      "title": "Limit"
    }
  },
  "required": [],
  "additionalProperties": false
}
```
