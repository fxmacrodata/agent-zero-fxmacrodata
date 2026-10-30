### fxmd_mcp_plot_visual_artifact

Build a generic MCP Apps chart from one or more FXMacroData endpoint families: arbitrary plots, multi-series charts, and actual-vs-consensus views that combine announcements with predictions. Supported series sources are announcements, predictions, forex, commodities, and cot. For example, USD policy-rate midpoint actuals against market consensus use one announcements series for `usd/policy_rate_midpoint` and one predictions series for `usd/policy_rate_midpoint` with `prediction_class=forecaster_survey`. The tool does not fetch arbitrary URLs or run custom chart code; it only composes approved FXMacroData API surfaces into the comparison chart app. Access: USD is available without an API key; every other currency returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "query": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional natural-language request to preserve in the payload title/context.",
      "examples": [
        "plot USD policy-rate midpoint actual vs market consensus",
        "compare AUD and USD inflation"
      ]
    },
    "series": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional list of series specs. Each spec supports `source` (announcements, predictions, forex, commodities, cot), `currency`, `indicator`, `base`, `quote`, `label`, `y_key`, `metric`, `prediction_class`, `prediction_source`, `start_date`, `end_date`, `limit`, `offset`, and `page`.",
      "examples": [
        [
          {
            "currency": "usd",
            "indicator": "policy_rate_midpoint",
            "label": "USD policy midpoint actual",
            "source": "announcements"
          },
          {
            "currency": "usd",
            "indicator": "policy_rate_midpoint",
            "label": "Dealer survey median",
            "prediction_class": "forecaster_survey",
            "source": "predictions"
          }
        ]
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
      "description": "Single-series source when `series` is omitted. Supported values: announcements, predictions, forex, commodities, cot.",
      "examples": [
        "announcements",
        "predictions",
        "forex"
      ]
    },
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
      "description": "Single-series currency for announcements, predictions, or COT. Supported macro currencies: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD. Supported COT currencies: AUD, CAD, CHF, EUR, GBP, JPY, NZD, USD, XAU.",
      "examples": [
        "usd",
        "eur",
        "gbp",
        "jpy"
      ]
    },
    "indicator": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Single-series indicator for announcements, predictions, or commodities. Supported macro indicators: afe_dollar_index, average_hourly_earnings, average_hourly_earnings_mom, balance_on_goods, balance_on_services, bank_lending_standards, bgcr, breakeven_inflation_rate, broad_dollar_index, broad_money, building_approvals, building_permits, business_confidence, business_inventories, capital_account_balance, cb_assets, commodity_price_energy, commodity_price_ex_energy, commodity_price_index, commodity_prices, construction_spending, consumer_confidence, core_inflation, core_inflation_median, core_inflation_mom, core_inflation_trim, core_pce, core_pce_mom, credit_growth, crude_oil_inventories, current_account_balance, dairy_exports, deposit_rates, distillate_inventories, durable_goods_orders, effr, eme_dollar_index, employment, employment_cost_index, exports, factory_orders, financial_account_balance, foreign_reserves, full_time_employment, fx_reserves, gasoline_inventories, gdp, gdp_growth_q4_yoy, gold_reserves, gov_bond_10y, gov_bond_15y, gov_bond_1_5m, gov_bond_1m, gov_bond_1y, gov_bond_20y, gov_bond_25y, gov_bond_2m, gov_bond_2y, gov_bond_30y, gov_bond_3m, gov_bond_3y, gov_bond_40y, gov_bond_4m, gov_bond_4y, gov_bond_5y, gov_bond_6m, gov_bond_6y, gov_bond_7y, gov_bond_8y, gov_bond_9y, government_debt, house_price_index, house_prices, household_credit, household_spending, housing_starts, import_prices, imports, industrial_production, inflation, inflation_linked_bond, inflation_mom, initial_jobless_claims, international_assets, international_liabilities, job_openings, m1, m2, m3, nairu, natural_gas_storage, net_foreign_asset_position, non_farm_payrolls, non_farm_payrolls_change, obfr, part_time_employment, participation_rate, pce, pce_mom, policy_rate, policy_rate_midpoint, policy_rate_mlf, policy_rate_mro, policy_rate_target_lower, ppi, primary_income_balance, productivity, real_yield_20y, real_yield_30y, real_yield_5y, real_yield_7y, retail_sales, retail_sales_control_group, retail_sales_ex_autos, retail_sales_ex_autos_and_gas, risk_free_rate, secondary_income_balance, sight_deposits, snb_balance_sheet, sofr_average_180d, sofr_average_30d, sofr_average_90d, sofr_index, terms_of_trade, tgcr, trade_balance, trade_weighted_index, trimmed_mean_inflation, unemployment, wage_price_index, wages, wholesale_inventories. Supported commodity indicators: crude_oil_inventories, distillate_inventories, gasoline_inventories, gold, natural_gas, natural_gas_storage, oil_brent, oil_wti, platinum, silver.",
      "examples": [
        "policy_rate",
        "inflation",
        "unemployment",
        "gdp"
      ]
    },
    "base": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Base currency for single-series forex plots. Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "eur",
        "aud",
        "usd"
      ]
    },
    "quote": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Quote currency for single-series forex plots. Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "usd",
        "jpy",
        "chf"
      ]
    },
    "prediction_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional legacy prediction-type filter for prediction series. Superseded by prediction_class.",
      "examples": [
        "fxmacrodata"
      ]
    },
    "prediction_source": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional prediction source filter for prediction series.",
      "examples": [
        "ny_fed_sme",
        "philly_fed_spf"
      ]
    },
    "x_axis": {
      "default": "date",
      "description": "Field to use as the shared x-axis. Supported: date, announcement_datetime, announcement_datetime_local, generated_at, observation_datetime.",
      "examples": [
        "date",
        "announcement_datetime"
      ],
      "type": "string"
    },
    "y_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Single-series metric field. Defaults by source: val for announcements and commodities, predicted_value for predictions, rate for forex, noncommercial_net for COT.",
      "examples": [
        "val",
        "predicted_value",
        "rate"
      ]
    },
    "y_label": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional y-axis label for the chart.",
      "examples": [
        "Policy Rate Midpoint",
        "Value"
      ]
    },
    "title": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional chart title. Defaults to query or an auto-generated title.",
      "examples": [
        "USD policy-rate actual vs consensus"
      ]
    },
    "chart_kind": {
      "default": "line",
      "description": "Initial chart view. Supported: line, area, bar, dot, step.",
      "examples": [
        "line",
        "step"
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
    "limit": {
      "default": 20,
      "description": "Maximum rows per source. Defaults to 20; maximum 100.",
      "examples": [
        20,
        100
      ],
      "maximum": 100,
      "minimum": 1,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Zero-based row offset per source.",
      "examples": [
        0,
        20
      ],
      "minimum": 0,
      "type": "integer"
    },
    "page": {
      "anyOf": [
        {
          "minimum": 1,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "One-based page number per source.",
      "examples": [
        1
      ]
    }
  },
  "type": "object",
  "title": "plot_visual_artifactArguments"
}
```
