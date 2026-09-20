# Data Dictionary & Schema Specification

| Field Name | Type | Nullable | Description & Example |
| :--- | :--- | :--- | :--- |
| `retailer` | STRING | NO | Primary retailer brand (`"Walmart"` or `"Target"`). |
| `item_id` | STRING | NO | Retailer primary product key (Walmart Item ID or Target TCIN, e.g. `"10315840"`). |
| `upc_gtin` | STRING | YES | 8 to 14-digit Global Trade Item Number / UPC-A barcode with leading zeros intact (e.g. `"078742351865"`). |
| `title` | STRING | NO | Normalized product title with decoded HTML entities and cleaned whitespace. |
| `brand` | STRING | NO | Verified manufacturer or private label brand name (e.g. `"Great Value"`, `"Figmint"`). |
| `category` | STRING | NO | Standard retail taxonomy category (e.g. `"Frozen Meat"`, `"Cooking Utensil Sets"`). |
| `price_usd` | FLOAT | YES | Observed base retail price in US Dollars (e.g. `12.97`). |
| `currency` | STRING | NO | Currency standard ISO 4217 (`"USD"`). |
| `in_stock` | INTEGER | NO | In-stock inventory indicator (`1` = In Stock, `0` = Out of Stock). |
| `product_url` | STRING | NO | Canonical direct storefront URL without affiliate tracking parameters. |
| `is_verified_1p` | INTEGER | NO | First-party verification flag (`1` = Sold directly by retailer). |
| `last_verified_utc` | STRING | NO | ISO 8601 UTC timestamp of last verification. |
