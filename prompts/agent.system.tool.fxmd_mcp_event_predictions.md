### fxmd_mcp_event_predictions

Return stored forecasts, consensus-style predictions, central-bank projections, survey forecasts, IMF forecasts, nowcasts, or FXMacroData blended predictions for macro announcements, for actual-vs-consensus, prior-vs-forecast, or event-surprise context. Rows are keyed by announcement_id/date/indicator and include prediction source metadata. Supported currencies: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD. The `indicator` parameter lists the accepted indicator slugs. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "currency": {
      "description": "3-letter ISO currency code (case-insensitive). Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "usd",
        "eur",
        "gbp",
        "jpy"
      ],
      "type": "string"
    },
    "indicator": {
      "description": "Required indicator slug. Currency-wide prediction reads are not supported. Supported: afe_dollar_index, average_hourly_earnings, average_hourly_earnings_mom, balance_on_goods, balance_on_services, bank_lending_standards, bgcr, breakeven_inflation_rate, broad_dollar_index, broad_money, building_approvals, building_permits, business_confidence, business_inventories, capital_account_balance, cb_assets, commodity_price_energy, commodity_price_ex_energy, commodity_price_index, commodity_prices, construction_spending, consumer_confidence, core_inflation, core_inflation_median, core_inflation_mom, core_inflation_trim, core_pce, core_pce_mom, credit_growth, crude_oil_inventories, current_account_balance, dairy_exports, deposit_rates, distillate_inventories, durable_goods_orders, effr, eme_dollar_index, employment, employment_cost_index, exports, factory_orders, financial_account_balance, foreign_reserves, full_time_employment, fx_reserves, gasoline_inventories, gdp, gdp_growth_q4_yoy, gold_reserves, gov_bond_10y, gov_bond_15y, gov_bond_1_5m, gov_bond_1m, gov_bond_1y, gov_bond_20y, gov_bond_25y, gov_bond_2m, gov_bond_2y, gov_bond_30y, gov_bond_3m, gov_bond_3y, gov_bond_40y, gov_bond_4m, gov_bond_4y, gov_bond_5y, gov_bond_6m, gov_bond_6y, gov_bond_7y, gov_bond_8y, gov_bond_9y, government_debt, house_price_index, house_prices, household_credit, household_spending, housing_starts, import_prices, imports, industrial_production, inflation, inflation_linked_bond, inflation_mom, initial_jobless_claims, international_assets, international_liabilities, job_openings, m1, m2, m3, nairu, natural_gas_storage, net_foreign_asset_position, non_farm_payrolls, non_farm_payrolls_change, obfr, part_time_employment, participation_rate, pce, pce_mom, policy_rate, policy_rate_midpoint, policy_rate_mlf, policy_rate_mro, policy_rate_target_lower, ppi, primary_income_balance, productivity, real_yield_20y, real_yield_30y, real_yield_5y, real_yield_7y, retail_sales, retail_sales_control_group, retail_sales_ex_autos, retail_sales_ex_autos_and_gas, risk_free_rate, secondary_income_balance, sight_deposits, snb_balance_sheet, sofr_average_180d, sofr_average_30d, sofr_average_90d, sofr_index, terms_of_trade, tgcr, trade_balance, trade_weighted_index, trimmed_mean_inflation, unemployment, wage_price_index, wages, wholesale_inventories.",
      "examples": [
        "policy_rate",
        "inflation",
        "unemployment",
        "gdp"
      ],
      "type": "string"
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
      "description": "Optional legacy forecast-type filter, kept for existing clients. Superseded by prediction_class: compiled_consensus, forecaster_survey, expectations_survey, market_implied, model_nowcast, central_bank_projection, institutional_projection or fxmacrodata.",
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
      "description": "Optional source slug filter, for example ecb_spf or philly_fed_spf.",
      "examples": [
        "ecb_spf",
        "philly_fed_spf"
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
      "description": "Optional inclusive lower bound by reference-period date, YYYY-MM-DD.",
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
      "description": "Optional inclusive upper bound by reference-period date, YYYY-MM-DD.",
      "examples": [
        "2020-01-01",
        "2024-06-30"
      ]
    },
    "limit": {
      "default": 20,
      "description": "Maximum prediction groups to return. Defaults to 20; maximum 100.",
      "examples": [
        20
      ],
      "maximum": 100,
      "minimum": 1,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Zero-based prediction-group offset.",
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
      "description": "One-based page number. When supplied, overrides offset.",
      "examples": [
        1
      ]
    },
    "prediction_class": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Forecast production class: compiled_consensus, forecaster_survey, expectations_survey, market_implied, model_nowcast, central_bank_projection, institutional_projection or fxmacrodata."
    },
    "as_of": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Historical publication cutoff with explicit timezone, or YYYY-MM-DD at UTC midnight. Later forecasts are excluded."
    },
    "event_compatible_only": {
      "default": false,
      "description": "Restrict event-linked data to verified matching target periods, units and economic concepts. Native official_forecasts remain a separate section.",
      "type": "boolean"
    },
    "pre_release_only": {
      "default": true,
      "description": "Require event-linked forecasts to have been generated before the announcement.",
      "type": "boolean"
    },
    "official_limit": {
      "default": 500,
      "description": "Maximum native-period official forecasts; 0 omits this section. Inspect official_forecasts_truncated.",
      "maximum": 2000,
      "minimum": 0,
      "type": "integer"
    },
    "before_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Exclusive period-date cursor for event-linked groups; use the prior response's next_cursor."
    },
    "seasonality": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Seasonal adjustment selector, matching the announcement series."
    },
    "frequency": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Returned change basis selector, matching the announcement series."
    },
    "annualization": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Annualization selector, matching the announcement series."
    },
    "period_aggregation": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Period aggregation selector, matching the announcement series."
    },
    "basis": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Real or nominal selector, matching the announcement series."
    }
  },
  "required": [
    "currency",
    "indicator"
  ],
  "type": "object",
  "title": "event_predictionsArguments"
}
```
