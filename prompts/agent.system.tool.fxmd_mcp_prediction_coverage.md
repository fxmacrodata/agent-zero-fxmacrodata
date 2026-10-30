### fxmd_mcp_prediction_coverage

List which publishers produce pre-release forecasts for a currency's indicators, what class of forecast each one is (compiled consensus, forecaster survey, market implied, model nowcast, central-bank projection), whether any of them is a genuine consensus, and how far the verified archive runs. Suited to questions about whether a consensus, forecast or estimate exists for a release, such as 'do you have the consensus for US CPI' or 'what forecast do you have for payrolls'. It needs no API key and works for every served currency. It returns no forecast values: those require a subscription. Its answer distinguishes two cases: no publisher produces this forecast for anybody (no subscription adds it), versus the data exists and is behind the paywall. A pair listed here exists in the verified archive. Access: free for every currency, no API key required. It returns coverage metadata only; forecast values need a subscription.

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
      "description": "Optional 3-letter currency code. Omit for the cross-currency summary; pass one for per-indicator detail.",
      "examples": [
        "usd",
        "eur",
        "jpy"
      ]
    }
  },
  "type": "object",
  "title": "prediction_coverageArguments"
}
```
