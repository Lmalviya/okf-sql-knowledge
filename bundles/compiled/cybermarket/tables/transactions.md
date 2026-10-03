---
type: PostgreSQL Table
title: transactions
description: '19 columns: rectag, eventstamp, paymethod, payamtusd, txfeeusd, escrowused, escrowhrs, multisigflag, txstatus, txfinishhrs, shipmethod, shipregionsrc, shipregiondst, crossborderflag, routecomplexity. Joins to buyers, markets, products.'
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
| `txregistry` | character varying, primary key | Primary key (VARCHAR(30)) for each transaction (e.g., 'TX-abc123'). |
| `rectag` | character varying | A unique VARCHAR(30) record ID for external references (e.g., 'Record-90876'). |
| `eventstamp` | timestamp without time zone | A TIMESTAMP capturing the transaction creation or logging time (e.g., '2025-03-01 12:00:00'). |
| `paymethod` | USER-DEFINED | An enum (PayMethod_enum) naming the payment type (Crypto_A, Crypto_B, Crypto_C, Token). |
| `payamtusd` | numeric | A NUMERIC(14,2) capturing the transaction’s total payment amount in USD (e.g., 10000.00). |
| `txfeeusd` | numeric | A NUMERIC(10,2) for fees in USD (e.g., 15.50). |
| `escrowused` | USER-DEFINED | An enum (EscrowUsed_enum) indicating if escrow was used (Yes, No). |
| `escrowhrs` | smallint | A SMALLINT for how many hours funds remain in escrow (e.g., 72). |
| `multisigflag` | USER-DEFINED | An enum (MultiSigFlag_enum) capturing whether multi-signature was enabled (Yes, No). |
| `txstatus` | USER-DEFINED | An enum (TxStatus_enum) showing transaction status (Pending, Cancelled, Completed, Disputed). |
| `txfinishhrs` | numeric | A NUMERIC(5,2) measuring how many hours until completion (e.g., 48.75). |
| `shipmethod` | USER-DEFINED | An enum (ShipMethod_enum) describing delivery approach (Express, Standard, Custom, Digital). |
| `shipregionsrc` | USER-DEFINED | An enum (ShipRegionSrc_enum) for the source region (Region_A, Region_B, Region_C, Unknown). |
| `shipregiondst` | USER-DEFINED | An enum (ShipRegionDst_enum) for the destination region (Region_X, Region_Y, Region_Z, Unknown). |
| `crossborderflag` | USER-DEFINED | An enum (CrossBorderFlag_enum) stating if it's an international transaction (Yes, No). |
| `routecomplexity` | USER-DEFINED | An enum (RouteComplexity_enum) describing shipping route complexity (Complex, Medium, Simple). |
| `mktref` | character varying | FK referencing Markets(MktRegistry). Identifies which market the transaction occurred on. |
| `prodref` | character varying | FK referencing Products(ProdRegistry). Ties transaction to a product listing. |
| `buyref` | character varying | FK referencing Buyers(BuyRegistry). Specifies the buyer who initiated the transaction. |

# Joins

* `buyref` references `buyregistry` in [buyers](/tables/buyers.md).
* `mktref` references `mktregistry` in [markets](/tables/markets.md).
* `prodref` references `prodregistry` in [products](/tables/products.md).

# Related knowledge

* [cybermarket|transactions|paymethod](/knowledge/cybermarket-transactions-paymethod.md)
* [cybermarket|transactions|txstatus](/knowledge/cybermarket-transactions-txstatus.md)
* [Transaction Anomaly Score (TAS)](/knowledge/transaction-anomaly-score.md)
* [Suspicious Transaction Pattern](/knowledge/suspicious-transaction-pattern.md)
* [Vendor Network Centrality (VNC)](/knowledge/vendor-network-centrality.md)
* [Product Risk Exposure (PRE)](/knowledge/product-risk-exposure.md)
* [Transaction Velocity Metric (TVM)](/knowledge/transaction-velocity-metric.md)
* [Market Diversification Score (MDS)](/knowledge/market-diversification-score.md)
* [Cross-Platform Risk Amplification (CPRA)](/knowledge/cross-platform-risk-amplification.md)
* [Market Kingpin](/knowledge/market-kingpin.md)
* [High-Exposure Product](/knowledge/high-exposure-product.md)
* [Flash Transaction Cluster](/knowledge/flash-transaction-cluster.md)
