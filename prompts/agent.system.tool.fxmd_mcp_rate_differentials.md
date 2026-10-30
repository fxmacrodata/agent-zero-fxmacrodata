### fxmd_mcp_rate_differentials

Return the stored or derived rate differential for one FX pair, with the measure, rate type, curve family, and tenor metadata that define it. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "base": {
      "description": "Base currency code.",
      "examples": [
        "aud"
      ],
      "type": "string"
    },
    "quote": {
      "description": "Quote currency code.",
      "examples": [
        "usd"
      ],
      "type": "string"
    },
    "measure": {
      "default": "auto",
      "description": "Shared rate measure to compare across the pair.",
      "examples": [
        "auto",
        "policy_rate",
        "gov_bond_10y"
      ],
      "type": "string"
    },
    "rate_type": {
      "default": "spot",
      "description": "Differential type: spot or forward.",
      "examples": [
        "spot",
        "forward"
      ],
      "type": "string"
    },
    "curve_family": {
      "default": "government_nominal",
      "description": "Curve family when rate_type is forward.",
      "type": "string"
    },
    "start_tenor_years": {
      "default": 2,
      "description": "Start tenor in years for forward differentials.",
      "type": "number"
    },
    "end_tenor_years": {
      "default": 5,
      "description": "End tenor in years for forward differentials.",
      "type": "number"
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
      "description": "Optional inclusive start date, YYYY-MM-DD."
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
      "description": "Optional inclusive end date, YYYY-MM-DD."
    },
    "limit": {
      "default": 20,
      "description": "Maximum rows to return.",
      "maximum": 100,
      "minimum": 1,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Zero-based row offset.",
      "minimum": 0,
      "type": "integer"
    }
  },
  "required": [
    "base",
    "quote"
  ],
  "type": "object",
  "title": "rate_differentialsArguments"
}
```
