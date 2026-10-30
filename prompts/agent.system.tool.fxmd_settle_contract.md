### fxmd_settle_contract

Settle a contract template for one release

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
  "properties": {
    "contract_id": {
      "type": "string",
      "examples": [
        "usd_cpi_yoy"
      ],
      "title": "Contract Id",
      "enum": [
        "aud_rba_decision",
        "cad_boc_decision",
        "eur_ecb_decision",
        "eur_hicp_flash_yoy",
        "gbp_boe_decision",
        "gbp_cpi_yoy",
        "jpy_boj_decision",
        "usd_core_cpi_mom",
        "usd_core_cpi_yoy",
        "usd_core_pce_mom",
        "usd_cpi_mom",
        "usd_cpi_yoy",
        "usd_fed_decision",
        "usd_gdp_advance_qoq_saar",
        "usd_initial_jobless_claims",
        "usd_nonfarm_payrolls_change",
        "usd_pce_yoy",
        "usd_unemployment_rate"
      ],
      "example": "aud_rba_decision",
      "description": "Required path parameter. Allowed values: aud_rba_decision, cad_boc_decision, eur_ecb_decision, eur_hicp_flash_yoy, gbp_boe_decision, gbp_cpi_yoy, jpy_boj_decision, usd_core_cpi_mom, usd_core_cpi_yoy, usd_core_pce_mom, usd_cpi_mom, usd_cpi_yoy, usd_fed_decision, usd_gdp_advance_qoq_saar, usd_initial_jobless_claims, usd_nonfarm_payrolls_change, usd_pce_yoy, usd_unemployment_rate."
    },
    "period": {
      "type": "string",
      "description": "Optional query parameter. Reference date of the release (YYYY-MM-DD), or `latest`.",
      "examples": [
        "2026-09-30"
      ],
      "default": "latest",
      "title": "Period"
    },
    "strike": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Contract strike in the series unit.",
      "title": "Strike"
    },
    "comparison": {
      "enum": [
        "above",
        "at_or_above",
        "below",
        "at_or_below",
        "equal"
      ],
      "type": "string",
      "description": "Optional query parameter. How the published value is compared with the strike.",
      "default": "above",
      "title": "Comparison"
    },
    "currency": {
      "type": "string",
      "title": "Currency",
      "description": "Required query parameter."
    }
  },
  "required": [
    "contract_id",
    "currency"
  ],
  "additionalProperties": false
}
```
