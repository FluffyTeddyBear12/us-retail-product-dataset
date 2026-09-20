# US Retail Product & Barcode Dataset (Walmart & Target Verified 1P)

[![Dataset License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CSV / JSONL / SQLite](https://img.shields.io/badge/Formats-CSV%20%7C%20JSONL%20%7C%20SQLite-green.svg)](#)
[![Commercial Store](https://img.shields.io/badge/Gumroad-Commercial%20Data%20Fleet-orange.svg)](https://jimmied.gumroad.com/l/bsdipe)

A clean, normalized, 1P-verified retail product catalog covering major US retailers (**Walmart** and **Target**). Designed for data scientists, machine learning engineers, retail arbitrageurs, and e-commerce developers.

---

## 🚀 Why This Dataset?

Most scraped retail catalogs online are messy:
- Barcode leading zeros are truncated (`078742...` becomes `78742...`).
- 404 dead links and spam 3P marketplace vendors.
- Cluttered with tracking tokens and session IDs.

This dataset provides **institutional-grade clean data**:
1. **100% 1P Verified:** Only authentic first-party retail items sold directly by Walmart and Target.
2. **Preserved UPC/GTIN Barcodes:** Formatted as strict strings with UTF-8 BOM to prevent Excel truncation.
3. **Clean Canonical URLs:** Direct storefront links with zero tracking tokens.
4. **Normalized Schema:** Cleaned brands, categories, prices, and stock indicators.

---

## 📊 Free 100-Row Sample Preview

A free 100-row preview sample is included in this repository: [`free_sample_preview_100_rows.csv`](free_sample_preview_100_rows.csv).

| retailer | item_id | upc_gtin | brand | title | price_usd | in_stock |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Walmart | 10450114 | 078742351865 | Great Value | Great Value Whole Vitamin D Milk, 1 Gallon | 2.46 | 1 |
| Target | 90000007 | 198101240828 | Figmint | 2pk Mini Spatula Set Matte Black - Figmint™ | 10.00 | 1 |
| Walmart | 10291025 | 033200011101 | Arm & Hammer | Arm & Hammer Pure Baking Soda, 1 lb | 1.52 | 1 |
| Target | 070059348 | 052181484445 | Safety 1st | Safety 1st White Plastic Drawer Latches (4-Pack) | 6.99 | 1 |

---

## ⚡ Get the Full 62,500+ Master Catalog & Arbitrage Matches

Looking for the complete production database or cross-store arbitrage matching table for your application or business?

👉 **[Download the Master Catalog on Gumroad (4 Tiers from $19 to $79)](https://jimmied.gumroad.com/l/bsdipe)**

**Commercial Tiers Available:**
1. **Developer Starter Pack ($19.00):** 10,000 SKUs (5k Walmart + 5k Target) with 100% verified barcodes.
2. **Walmart 1P Sovereign Master Index ($39.00):** Full 14,000+ Walmart 1P catalog with 90%+ GTIN barcodes and shelf prices.
3. **Target Sovereign Master Index ($39.00):** Full 48,900+ Target catalog with TCIN, 19,300+ DPCI codes, and barcodes.
4. **Master Arbitrage Dual-Fleet Bundle ($79.00):** Complete 62,500+ catalog + Unified Cross-Store Barcode Match Table with price spread analysis.

**Formats included in every tier:**
- Formatted table in **CSV (UTF-8 BOM)** for native Excel support.
- Streaming **JSONL** file for big-data pipelines (BigQuery, Pandas, Elasticsearch).
- Pre-indexed **SQLite 3 database** with B-Tree indexes on `upc_gtin`, `brand`, and `category`.
- Full perpetual commercial license.

---

## 🛠️ Quickstart (Python & SQLite)

Run the included `quickstart.py` to inspect the sample data:

```python
import csv

with open("free_sample_preview_100_rows.csv", mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        if i >= 5:
            break
        print(f"[{row['retailer']}] {row['title']} | UPC: {row['upc_gtin']} | ${row['price_usd']}")
```

---

## 📄 License

This free preview repository is licensed under the [MIT License](LICENSE). Commercial production tiers are licensed under the NestStock Commercial Data License.
