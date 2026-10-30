### fxmd_mcp_rate_curve

Return official government-nominal curve nodes, slopes, or derived forward segments for one currency. This is a subscriber data tool and preserves the endpoint's requested view and method metadata. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "currency": {
      "description": "3-letter currency code.",
      "examples": [
        "usd",
        "eur",
        "gbp",
        "jpy"
      ],
      "type": "string"
    },
    "curve_family": {
      "default": "government_nominal",
      "description": "Official curve family.",
      "type": "string"
    },
    "metric": {
      "default": "spot",
      "description": "Curve metric.",
      "type": "string"
    },
    "view": {
      "default": "nodes",
      "description": "Curve view: nodes, slopes, or forwards.",
      "examples": [
        "nodes",
        "slopes",
        "forwards"
      ],
      "type": "string"
    },
    "method": {
      "default": "derived_from_spot_nodes",
      "description": "Forward derivation method when view is forwards.",
      "type": "string"
    },
    "date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional target date, YYYY-MM-DD."
    }
  },
  "required": [
    "currency"
  ],
  "type": "object",
  "title": "rate_curveArguments"
}
```
