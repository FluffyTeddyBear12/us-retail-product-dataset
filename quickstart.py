"""Quickstart demo script for testing the US Retail Product Dataset sample."""

import csv
from pathlib import Path

SAMPLE_FILE = Path(__file__).parent / "free_sample_preview_100_rows.csv"

if not SAMPLE_FILE.exists():
    print(f"[!] Sample file not found at: {SAMPLE_FILE}")
    exit(1)

print("=" * 70)
print(" US Retail Product Dataset — Free Sample Preview")
print("=" * 70)

with open(SAMPLE_FILE, mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"[*] Loaded {len(rows)} sample records.")
print("\nFirst 5 Sample Records:\n")

for i, row in enumerate(rows[:5], 1):
    print(f"{i}. [{row['retailer']}] {row['title']}")
    print(f"   Brand: {row['brand']} | Category: {row['category']}")
    print(f"   UPC: {row['upc_gtin']} | Price: ${row['price_usd']} | In Stock: {bool(int(row['in_stock']))}")
    print(f"   URL: {row['product_url']}\n")

print("-" * 70)
print("👉 For the full 50,000+ Master Catalog: see README.md")
