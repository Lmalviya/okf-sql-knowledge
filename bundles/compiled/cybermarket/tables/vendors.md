---
type: PostgreSQL Table
title: vendors
description: '11 columns: vendspan, vendrate, vendtxcount, vendsucccount, venddisputecount, vendplacecount, vendpaymethods, vendchecklvl, vendlastmoment. Joins to markets.'
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
| `vendregistry` | character varying, primary key | Primary key (VARCHAR(30)) uniquely identifying a vendor (e.g., 'VEND-Abc123'). |
| `vendspan` | integer | An INT indicating how many days the vendor has been active (e.g., 120). |
| `vendrate` | numeric | A NUMERIC(4,2) (0–99.99) rating for the vendor based on reviews (e.g., 92.75). |
| `vendtxcount` | integer | An INT total number of completed transactions for the vendor (e.g., 3500). |
| `vendsucccount` | integer | An INT number of undisputed or successful transactions (e.g., 3400). |
| `venddisputecount` | integer | An INT number of disputed transactions (e.g., 100). |
| `vendplacecount` | smallint | A SMALLINT representing how many listings the vendor has created (e.g., 45). |
| `vendpaymethods` | smallint | A SMALLINT showing how many payment methods the vendor accepts (e.g., 3). |
| `vendchecklvl` | USER-DEFINED | An enum (VendCheckLvl_enum) describing the vendor’s verification tier (Basic, Advanced, Premium). |
| `vendlastmoment` | date | A DATE recording the vendor's last activity (e.g., '2025-03-15'). |
| `mktref` | character varying | FK referencing Markets(MktRegistry) linking this vendor to a specific market. |

# Joins

* `mktref` references `mktregistry` in [markets](/tables/markets.md).

# Related knowledge

* [cybermarket|vendors|vendchecklvl](/knowledge/cybermarket-vendors-vendchecklvl.md)
* [Vendor Trust Index (VTI)](/knowledge/vendor-trust-index.md)
* [Market Stability Index (MSI)](/knowledge/market-stability-index.md)
* [Trusted Vendor](/knowledge/trusted-vendor.md)
* [Market Migration Indicator](/knowledge/market-migration-indicator.md)
* [Vendor Network Centrality (VNC)](/knowledge/vendor-network-centrality.md)
* [Vendor Relationship Strength (VRS)](/knowledge/vendor-relationship-strength.md)
* [Cross-Platform Risk Amplification (CPRA)](/knowledge/cross-platform-risk-amplification.md)
* [Market Kingpin](/knowledge/market-kingpin.md)
* [Customer Loyalty Network](/knowledge/customer-loyalty-network.md)
