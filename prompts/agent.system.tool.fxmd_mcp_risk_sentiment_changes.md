### fxmd_mcp_risk_sentiment_changes

Poll retained risk-sentiment additions, score revisions, and input-metadata changes. Pass pagination.next_after_sequence as after_sequence on the next page or poll. Recording timestamps describe when FXMacroData stored each change; earlier untracked revisions and publisher publication times are unavailable. Access: free, no API key required.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "after_sequence": {
      "default": 0,
      "description": "Return recorded changes after this sequence, exclusively.",
      "examples": [
        0,
        25
      ],
      "minimum": 0,
      "type": "integer"
    },
    "limit": {
      "default": 20,
      "description": "Maximum retained changes per page. Defaults to 20; maximum 100.",
      "examples": [
        20,
        100
      ],
      "maximum": 100,
      "minimum": 1,
      "type": "integer"
    }
  },
  "type": "object",
  "title": "risk_sentiment_changesArguments"
}
```
