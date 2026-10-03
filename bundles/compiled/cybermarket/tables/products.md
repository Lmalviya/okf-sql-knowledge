---
type: PostgreSQL Table
title: products
description: '8 columns: prodtheme, prodsubcat, prodlistdays, prodpriceusd, prodqty. Joins to buyers, vendors.'
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_schema.txt
  title: cybermarket schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_column_meaning_base.json
  title: cybermarket column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `prodregistry` | character varying, primary key | Primary key (VARCHAR(30)) for each product listing (e.g., 'PROD-12345'). |
| `prodtheme` | USER-DEFINED | An enum (ProdTheme_enum) for the product's main category (Digital, Data, Service, Physical). |
| `prodsubcat` | USER-DEFINED | An enum (ProdSubcat_enum) specifying the product subcategory (Type_A, Type_B, Type_C, Type_D). |
| `prodlistdays` | integer | An INT showing how many days the listing has been on the market (e.g., 14). |
| `prodpriceusd` | numeric | A NUMERIC(10,2) price of the product in USD (e.g., 199.99). |
| `prodqty` | integer | An INT specifying available quantity (e.g., 500). |
| `vendref` | character varying | FK referencing Vendors(VendRegistry) indicating which vendor offers this product. |
| `buyref` | character varying | FK referencing Buyers(BuyRegistry), if reserved or linked to a specific buyer. |

# Joins

* `buyref` references `buyregistry` in [buyers](/tables/buyers.md).
* `vendref` references `vendregistry` in [vendors](/tables/vendors.md).

# Related knowledge

* [cybermarket|products|prodtheme](/knowledge/cybermarket-products-prodtheme.md)
* [Market Diversification Score (MDS)](/knowledge/market-diversification-score.md)
* [Diversified Marketplace](/knowledge/diversified-marketplace.md)
