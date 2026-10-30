### fxmd_mcp_commodities_visual_artifact

Returns commodity price history with MCP Apps chart metadata so compatible clients render an interactive commodity chart inline. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "indicator": {
      "description": "Commodity indicator slug. Supported: crude_oil_inventories, distillate_inventories, gasoline_inventories, gold, natural_gas, natural_gas_storage, oil_brent, oil_wti, platinum, silver.",
      "examples": [
        "crude_oil_inventories",
        "distillate_inventories",
        "gasoline_inventories",
        "gold",
        "natural_gas",
        "natural_gas_storage"
      ],
      "type": "string"
    },
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
      "description": "Inclusive lower bound, YYYY-MM-DD.",
      "examples": [
        "2020-01-01",
        "2024-06-30"
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
      "description": "Inclusive upper bound, YYYY-MM-DD.",
      "examples": [
        "2020-01-01",
        "2024-06-30"
      ]
    }
  },
  "required": [
    "indicator"
  ],
  "type": "object",
  "title": "commodities_visual_artifactArguments"
}
```
