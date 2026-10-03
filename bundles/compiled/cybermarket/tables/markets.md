---
type: PostgreSQL Table
title: markets
description: '13 columns: mktdenom, mktclass, mktspan, sizecluster, dlyflow, mthactive, vendcount, buycount, listtotal, interscore, esccomprate, market_status_reputation.'
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
| `mktregistry` | character varying, primary key | Primary key (VARCHAR(30)) uniquely identifying a specific market entry (e.g., 'MKT-AlphaBay'). |
| `mktdenom` | character varying | A descriptive name or label for the dark market (e.g., 'AlphaBay', 'DreamMarket'). |
| `mktclass` | USER-DEFINED | An enum (MktClass_enum) denoting the market's general class (Forum, Service, Marketplace, Exchange). |
| `mktspan` | integer | An INT representing how many days this market has been active (e.g., 345). |
| `sizecluster` | USER-DEFINED | An enum (SizeCluster_enum) labeling market size (Mega, Medium, Large, Small). |
| `dlyflow` | bigint | A BIGINT indicating daily transaction volume (e.g., 123456). |
| `mthactive` | bigint | A BIGINT counting monthly active users on the market (e.g., 500000). |
| `vendcount` | integer | An INT tally of how many vendors operate in this market (e.g., 15000). |
| `buycount` | integer | An INT count of buyer accounts on this market (e.g., 100000). |
| `listtotal` | bigint | A BIGINT total number of product or service listings (e.g., 250000). |
| `interscore` | numeric | A NUMERIC(6,3) (0–999.999) scoring the market's interaction or activity level (e.g., 458.234). |
| `esccomprate` | numeric | A NUMERIC(5,3) (0–999.999) measuring escrow completion rate (e.g., 95.745). |
| `market_status_reputation` | jsonb | JSONB column. Consolidated information regarding the market's operational status, community reputation, trust level, and compliance/enforcement metrics. |

# JSON fields

* `market_status_reputation.status`: An enum (MarketStatus_enum) capturing the market's status (Active, Under Investigation, Suspended, Closed).
* `market_status_reputation.reputation_score`: A NUMERIC(6,3) reputation or community rating (0.000–999.999).
* `market_status_reputation.trust_level`: An enum (RiskLevel_enum) describing overall trust/risk level (Low, Medium, High, Unknown).
* `market_status_reputation.community_trust_score`: A NUMERIC(4,2) (0–99.99) representing community trust (e.g., 85.40).
* `market_status_reputation.dispute_resolution_score`: A NUMERIC(4,1) (0–99.9) describing effectiveness of dispute resolution (e.g., 8.7).
* `market_status_reputation.compliance_metrics.rule_break_count`: A SMALLINT counting known rule or TOS violations (e.g., 27).
* `market_status_reputation.compliance_metrics.warning_count`: A SMALLINT tallying warnings issued to market participants (e.g., 53).
* `market_status_reputation.compliance_metrics.penalty_count`: A SMALLINT for how many penalties or bans were enforced (e.g., 10).
* `market_status_reputation.compliance_metrics.restriction_level`: An enum (AccountRestrictionLevel_enum) stating the restriction extent (Full, Partial).

# Related knowledge

* [cybermarket|markets|mktclass](/knowledge/cybermarket-markets-mktclass.md)
* [cybermarket|markets|sizecluster](/knowledge/cybermarket-markets-sizecluster.md)
* [Market Risk Score (MRS)](/knowledge/market-risk-score.md)
* [Transaction Anomaly Score (TAS)](/knowledge/transaction-anomaly-score.md)
* [Market Stability Index (MSI)](/knowledge/market-stability-index.md)
* [Market Migration Indicator](/knowledge/market-migration-indicator.md)
* [Market Vulnerability Index (MVI)](/knowledge/market-vulnerability-index.md)
* [Market Diversification Score (MDS)](/knowledge/market-diversification-score.md)
* [Cross-Platform Risk Amplification (CPRA)](/knowledge/cross-platform-risk-amplification.md)
* [Diversified Marketplace](/knowledge/diversified-marketplace.md)
