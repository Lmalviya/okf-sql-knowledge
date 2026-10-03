---
type: PostgreSQL Table
title: buyers
description: '9 columns: buyspan, buytxtally, buyspending, buyfreqcat, buychecklvl, buyriskrate. Joins to markets, vendors.'
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
| `buyregistry` | character varying, primary key | Primary key (VARCHAR(30)) for a buyer record (e.g., 'BUY-xyz890'). |
| `buyspan` | integer | An INT specifying how many days the buyer has been active (e.g., 60). |
| `buytxtally` | smallint | A SMALLINT counting how many purchases/transactions the buyer made (e.g., 25). |
| `buyspending` | USER-DEFINED | An enum (BuySpending_enum) describing spending pattern (Variable, High, Low, Medium). |
| `buyfreqcat` | USER-DEFINED | An enum (BuyFreqCat_enum) labeling purchase frequency (Heavy, Regular, One-time, Occasional). |
| `buychecklvl` | USER-DEFINED | An enum (BuyCheckLvl_enum) specifying buyer verification level (Advanced, Basic). |
| `buyriskrate` | numeric | A NUMERIC(5,2) measure of fraud or chargeback risk for this buyer (e.g., 82.50). |
| `mktref` | character varying | FK referencing Markets(MktRegistry), linking buyer to its main or home market. |
| `vendref` | character varying | FK referencing Vendors(VendRegistry), if the buyer is directly associated with a vendor. |

# Joins

* `mktref` references `mktregistry` in [markets](/tables/markets.md).
* `vendref` references `vendregistry` in [vendors](/tables/vendors.md).

# Related knowledge

* [Market Migration Indicator](/knowledge/market-migration-indicator.md)
* [Vendor Network Centrality (VNC)](/knowledge/vendor-network-centrality.md)
* [Cross-Platform Risk Amplification (CPRA)](/knowledge/cross-platform-risk-amplification.md)
* [Market Kingpin](/knowledge/market-kingpin.md)
