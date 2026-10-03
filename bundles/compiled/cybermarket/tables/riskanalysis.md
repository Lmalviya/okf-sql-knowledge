---
type: PostgreSQL Table
title: riskanalysis
description: '16 columns: fraudprob, moneyrisk, linkedtxcount, txchainlen, wallrisksc, wallage, wallbalusd, wallturnrt, txvel, profilecomplete, idverifyscore, feedbackauthscore, network_behavior_analytics. Joins to communication, transactions.'
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
| `riskregistry` | character varying, primary key | Primary key (VARCHAR(30)) for a risk analysis record (e.g., 'RA-abc123'). |
| `fraudprob` | numeric | A NUMERIC(5,3) fraud probability (0.000–99.999) (e.g., 45.210). |
| `moneyrisk` | USER-DEFINED | An enum (RiskLevel_enum) for money laundering risk (Low, Medium, High, Unknown). |
| `linkedtxcount` | smallint | A SMALLINT counting related or linked transactions (e.g., 7). |
| `txchainlen` | smallint | A SMALLINT measuring transaction chain length (e.g., 4). |
| `wallrisksc` | numeric | A NUMERIC(5,2) wallet risk score (e.g., 88.50). |
| `wallage` | integer | An INT indicating wallet age in days (e.g., 200). |
| `wallbalusd` | numeric | A NUMERIC(15,2) approximate wallet balance in USD (e.g., 12500.00). |
| `wallturnrt` | numeric | A NUMERIC(5,3) wallet turnover rate (e.g., 5.234). |
| `txvel` | numeric | A NUMERIC(6,2) transaction velocity (e.g., 245.67). |
| `profilecomplete` | numeric | A NUMERIC(4,1) (0–99.9) indicating completeness of associated profile data (e.g., 85.7). |
| `idverifyscore` | numeric | A NUMERIC(4,1) (0–99.9) for identity verification confidence (e.g., 40.2). |
| `feedbackauthscore` | numeric | A NUMERIC(4,1) (0–99.9) rating authenticity of feedback (e.g., 92.3). |
| `commref` | character varying | FK referencing Communication(CommRegistry). Links risk analysis to communication logs. |
| `txref` | character varying | FK referencing Transactions(TxRegistry). Ties the analysis to a transaction chain or record. |
| `network_behavior_analytics` | jsonb | JSONB column. Stores scores derived from analyzing network structure, transaction patterns, temporal activity, geographic distribution, and behavioral consistency associated with the risk profile. |

# JSON fields

* `network_behavior_analytics.transaction_pattern_category`: An enum (TxPatternCat_enum) describing transaction patterns (High-risk, Suspicious, Normal).
* `network_behavior_analytics.network_analysis.cluster_coefficient`: A NUMERIC(5,4) graph clustering coefficient (0.0000–0.9999) (e.g., 0.3421).
* `network_behavior_analytics.network_analysis.centrality_score`: A NUMERIC(6,3) (0–999.999) network centrality measure (e.g., 452.110).
* `network_behavior_analytics.network_analysis.connection_diversity`: A NUMERIC(6,2) measuring diversity of connections (e.g., 78.45).
* `network_behavior_analytics.behavioral_analysis.temporal_pattern_score`: A NUMERIC(5,2) analyzing temporal patterns (e.g., 60.25).
* `network_behavior_analytics.behavioral_analysis.geo_distribution_score`: A NUMERIC(5,1) geolocation distribution score (e.g., 45.3).
* `network_behavior_analytics.behavioral_analysis.behavior_consistency_score`: A NUMERIC(5,2) consistency of behavior across time (e.g., 70.90).

# Joins

* `commref` references `commregistry` in [communication](/tables/communication.md).
* `txref` references `txregistry` in [transactions](/tables/transactions.md).

# Related knowledge

* [cybermarket|riskanalysis|moneyrisk](/knowledge/cybermarket-riskanalysis-moneyrisk.md)
* [Wallet Risk Index (WRI)](/knowledge/wallet-risk-index.md)
* [Transaction Chain Risk (TCR)](/knowledge/transaction-chain-risk.md)
* [Investigation Priority Score (IPS)](/knowledge/investigation-priority-score.md)
* [Money Laundering Indicator](/knowledge/money-laundering-indicator.md)
* [Sophisticated Operational Security](/knowledge/sophisticated-operational-security.md)
* [Money Flow Complexity (MFC)](/knowledge/money-flow-complexity.md)
