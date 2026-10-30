### fxmd_mcp_risk_sentiment

Return the global risk-on/risk-off sentiment series used for FX regime analysis. The result includes a derived composite score, regime label, component contributions, pagination, and data_quality metadata. Suited to cross-asset regime context for high-beta, safe-haven, commodity, or USD-defensive FX conditions. Access: free, no API key required.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional inclusive start date in YYYY-MM-DD format.",
      "examples": [
        "2026-06-01"
      ]
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional inclusive end date in YYYY-MM-DD format.",
      "examples": [
        "2026-06-30"
      ]
    }
  },
  "type": "object",
  "title": "risk_sentimentArguments"
}
```
