### fxmd_mcp_policy_scenario_modeler_task

Run a policy-rate spread what-if scenario for an FX pair and estimate directional spot impact using an explicit heuristic elasticity assumption. Returns analysis in the tool response. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "base": {
      "description": "Base currency, 3-letter ISO code (case-insensitive). Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "eur",
        "gbp",
        "aud",
        "usd"
      ],
      "type": "string"
    },
    "quote": {
      "description": "Quote currency, 3-letter ISO code (case-insensitive). Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "usd",
        "jpy",
        "chf"
      ],
      "type": "string"
    },
    "shock_leg": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "base",
      "description": "Which leg receives the policy shock: base or quote.",
      "examples": [
        "base",
        "quote"
      ]
    },
    "shock_bps": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": 25.0,
      "description": "Policy shock size in basis points (100 bps = 1.00 percentage point).",
      "examples": [
        25.0,
        50.0,
        -25.0
      ]
    },
    "policy_shock_bps": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional alias for shock_bps for compatibility with host-side app payloads.",
      "examples": [
        25.0,
        50.0
      ]
    },
    "elasticity_per_100bps": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": 0.8,
      "description": "Heuristic percent change in FX spot for a 100 bps spread change. Used as a scenario assumption, not a forecast guarantee.",
      "examples": [
        0.5,
        0.8,
        1.2
      ]
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
      "description": "Optional inclusive lower bound, YYYY-MM-DD.",
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
      "description": "Optional inclusive upper bound, YYYY-MM-DD.",
      "examples": [
        "2020-01-01",
        "2024-06-30"
      ]
    }
  },
  "required": [
    "base",
    "quote"
  ],
  "type": "object",
  "title": "policy_scenario_modeler_taskArguments"
}
```
