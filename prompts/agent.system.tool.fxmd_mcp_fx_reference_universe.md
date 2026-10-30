### fxmd_mcp_fx_reference_universe

List the public FX reference-rate pair universe, optionally filtered by currency or source id, showing which pairs and sources have intraday reference-rate series. Access: free for every currency, no API key required.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "currency": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional 3-letter currency filter.",
      "examples": [
        "usd"
      ]
    },
    "source": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional official source id filter.",
      "examples": [
        "ecb_eurofxref_daily"
      ]
    }
  },
  "type": "object",
  "title": "fx_reference_universeArguments"
}
```
