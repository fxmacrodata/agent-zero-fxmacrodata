### fxmd_mcp_indicator_query

Get a paginated historical time series of a single macroeconomic indicator for a currency, sourced directly from the official central bank or statistical agency. Covers CPI/inflation, GDP, unemployment, policy rates, bond yields, payrolls, retail sales, PCE, PPI, trade balance, current account, money supply, and similar series. Each row returns `date` (economic reference period), `val` (numeric), and separate publication evidence. The `as_of` parameter restricts results to historically eligible values; current values can include later revisions. Returns raw rows without chart metadata. Each call returns one page, newest first: 100 rows when `start_date` is set, otherwise 20 (`limit` overrides, maximum 100). A page is not the full history. When `pagination.has_more` is true the result has a `partial_page` object: `partial_page.next_call` holds the exact arguments for the next page and `partial_page.pages_remaining` gives the number of pages left. Responses default to official-source rows only; prohibited private aggregator rows are always removed. USD indicators are free; non-USD requires an API key. Supported currencies: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD. The `indicator` parameter lists the accepted indicator slugs. Access: USD is available without an API key; every other currency returns subscription_required with a subscribe link.

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
      "description": "3-letter ISO currency code (case-insensitive). Optional if `slug` is provided as a `\"usd:cpi\"`-style compound. Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
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
      "description": "Indicator slug for the given currency. Optional if `slug` is provided as a `\"usd:cpi\"`-style compound. Supported: afe_dollar_index, average_hourly_earnings, average_hourly_earnings_mom, balance_on_goods, balance_on_services, bank_lending_standards, bgcr, breakeven_inflation_rate, broad_dollar_index, broad_money, building_approvals, building_permits, business_confidence, business_inventories, capital_account_balance, cb_assets, commodity_price_energy, commodity_price_ex_energy, commodity_price_index, commodity_prices, construction_spending, consumer_confidence, core_inflation, core_inflation_median, core_inflation_mom, core_inflation_trim, core_pce, core_pce_mom, credit_growth, crude_oil_inventories, current_account_balance, dairy_exports, deposit_rates, distillate_inventories, durable_goods_orders, effr, eme_dollar_index, employment, employment_cost_index, exports, factory_orders, financial_account_balance, foreign_reserves, full_time_employment, fx_reserves, gasoline_inventories, gdp, gdp_growth_q4_yoy, gold_reserves, gov_bond_10y, gov_bond_15y, gov_bond_1_5m, gov_bond_1m, gov_bond_1y, gov_bond_20y, gov_bond_25y, gov_bond_2m, gov_bond_2y, gov_bond_30y, gov_bond_3m, gov_bond_3y, gov_bond_40y, gov_bond_4m, gov_bond_4y, gov_bond_5y, gov_bond_6m, gov_bond_6y, gov_bond_7y, gov_bond_8y, gov_bond_9y, government_debt, house_price_index, house_prices, household_credit, household_spending, housing_starts, import_prices, imports, industrial_production, inflation, inflation_linked_bond, inflation_mom, initial_jobless_claims, international_assets, international_liabilities, job_openings, m1, m2, m3, nairu, natural_gas_storage, net_foreign_asset_position, non_farm_payrolls, non_farm_payrolls_change, obfr, part_time_employment, participation_rate, pce, pce_mom, policy_rate, policy_rate_midpoint, policy_rate_mlf, policy_rate_mro, policy_rate_target_lower, ppi, primary_income_balance, productivity, real_yield_20y, real_yield_30y, real_yield_5y, real_yield_7y, retail_sales, retail_sales_control_group, retail_sales_ex_autos, retail_sales_ex_autos_and_gas, risk_free_rate, secondary_income_balance, sight_deposits, snb_balance_sheet, sofr_average_180d, sofr_average_30d, sofr_average_90d, sofr_index, terms_of_trade, tgcr, trade_balance, trade_weighted_index, trimmed_mean_inflation, unemployment, wage_price_index, wages, wholesale_inventories.",
      "examples": [
        "policy_rate",
        "inflation",
        "unemployment",
        "gdp"
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
      "anyOf": [
        {
          "maximum": 100,
          "minimum": 1,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Rows per page, newest first, maximum 100. Unset means 100 when `start_date` is set, otherwise 20.",
      "examples": [
        1,
        100
      ]
    },
    "offset": {
      "default": 0,
      "description": "Zero-based row offset after most-recent-first ordering. Take it from `partial_page.next_call`.",
      "examples": [
        0,
        1000
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
      "description": "One-based page number. When supplied, the REST endpoint derives offset as `(page - 1) * limit`.",
      "examples": [
        1,
        2
      ]
    },
    "slug": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional compound `\"<currency>:<indicator>\"` slug (e.g. `\"usd:cpi\"`, `\"jpy:policy_rate\"`). Many small / open tool-calling models concatenate the two parts anyway. When supplied, overrides `currency` and `indicator`.",
      "examples": [
        "usd:cpi",
        "jpy:policy_rate",
        "eur:gdp"
      ]
    },
    "official_only": {
      "default": true,
      "description": "When true, return only official-source rows and remove explicit fallback observations. Prohibited private aggregator rows are always removed.",
      "examples": [
        true
      ],
      "type": "boolean"
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
      "description": "Historical decision cutoff with explicit timezone, or YYYY-MM-DD at UTC midnight; verifies vintages before returning rows."
    },
    "availability": {
      "default": "public",
      "description": "Replay clock: public or captured. Used with as_of.",
      "type": "string"
    },
    "dataset_version": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional content version; use the first page's version on subsequent pages to reject changed data."
    },
    "revisions": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Revision view: latest, first, final or all. Historical replay uses latest among vintages eligible at as_of."
    },
    "series_mode": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Series mode: canonical or raw. Historical replay defaults to raw."
    },
    "value_mode": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Value mode: normalized or source. Historical replay defaults to unchanged source values and requires raw series mode."
    }
  },
  "type": "object",
  "title": "indicator_queryArguments"
}
```
