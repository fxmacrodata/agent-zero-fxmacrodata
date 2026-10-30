### fxmd_mcp_fx_backtest_task

Run a spot-only FX backtest using historical policy-rate-differential and/or lagged momentum signals. Downloads complete histories, verifies vintages and price coverage, and charges opening, rebalancing and closing costs. The carry signal does not include funding income or broker rollover. Returns analysis in the tool response. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "base": {
      "description": "Base currency, 3-letter ISO code. Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "eur",
        "gbp",
        "aud"
      ],
      "type": "string"
    },
    "quote": {
      "description": "Quote currency, 3-letter ISO code. Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "usd",
        "jpy",
        "chf"
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
    },
    "strategy": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "carry_momentum",
      "description": "Signal mode: carry, momentum, or carry_momentum.",
      "examples": [
        "carry_momentum",
        "carry",
        "momentum"
      ]
    },
    "momentum_lookback": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 5,
      "description": "Momentum lookback in observations for the momentum signal.",
      "examples": [
        5,
        10,
        20
      ]
    },
    "transaction_cost_bps": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": 2.0,
      "description": "Per-side transaction cost in basis points applied on position changes.",
      "examples": [
        1.0,
        2.0,
        5.0
      ]
    },
    "initial_capital": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": 100000.0,
      "description": "Starting capital for equity-curve calculations.",
      "examples": [
        10000.0,
        100000.0
      ]
    },
    "event_gated": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "When true, allow positions only after verified historical policy publications for either currency. This does not use future calendars or trade before a release.",
      "examples": [
        true,
        false
      ]
    },
    "event_window_days": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 1,
      "description": "Additional calendar days after the first UTC decision following publication; 0 permits that first day only.",
      "examples": [
        0,
        1,
        2
      ]
    }
  },
  "required": [
    "base",
    "quote"
  ],
  "type": "object",
  "title": "fx_backtest_taskArguments"
}
```
