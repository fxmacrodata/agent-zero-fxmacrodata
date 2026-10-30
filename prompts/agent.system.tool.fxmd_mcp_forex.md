### fxmd_mcp_forex

Get raw historical FX spot-rate rows for a currency pair (e.g. EUR/USD, USD/JPY) as a plain-text table, raw rows, exact values, or JSON-like data, with optional technical-indicator series (SMA, EMA, RSI, MACD, Bollinger Bands, etc.) computed from spot. Returns data only, without chart metadata. Daily granularity from official central-bank reference rates with full multi-year history. Supported currencies (lowercase 3-letter codes): AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD. The optional `indicators` parameter accepts a comma-separated list of technical indicator slugs to attach to each row. Supported indicator values: adx_14, atr_14, bollinger_bands, cci_20, donchian_20, ema_12, ema_20, ema_200, ema_26, ema_50, macd, macd_histogram, macd_signal, rsi_14, sma_20, sma_200, sma_50, stochastic_14_3, williams_r_14, all. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

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
      "description": "Inclusive lower bound, YYYY-MM-DD. Defaults to ~5 years ago.",
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
      "description": "Inclusive upper bound, YYYY-MM-DD. Defaults to today.",
      "examples": [
        "2020-01-01",
        "2024-06-30"
      ]
    },
    "indicators": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Comma-separated technical-indicator slugs to attach to each row. Supported: adx_14, atr_14, bollinger_bands, cci_20, donchian_20, ema_12, ema_20, ema_200, ema_26, ema_50, macd, macd_histogram, macd_signal, rsi_14, sma_20, sma_200, sma_50, stochastic_14_3, williams_r_14, all.",
      "examples": [
        "sma_50,sma_200",
        "rsi_14",
        "ema_20,atr_14"
      ]
    }
  },
  "required": [
    "base",
    "quote"
  ],
  "type": "object",
  "title": "forexArguments"
}
```
