### fxmd_mcp_latest_announcements

Return the latest stored macroeconomic value for every available indicator in one currency, as a compact current macro snapshot. An unverified announcement_datetime has unproven origin; it is neither a verified scheduled time nor observed actual publication. Report absent schedule, publication and ingestion evidence as unknown, and latency as not measured. Access: USD is available without an API key; every other currency returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "currency": {
      "description": "3-letter ISO currency code (case-insensitive).",
      "examples": [
        "usd",
        "eur",
        "gbp",
        "jpy"
      ],
      "type": "string"
    }
  },
  "required": [
    "currency"
  ],
  "type": "object",
  "title": "latest_announcementsArguments"
}
```
