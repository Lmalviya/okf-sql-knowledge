---
type: PostgreSQL Table
title: financials
description: '13 columns: budgetallotusd, fundsutilpct, costbeneusd, opscostsusd, transportcostsusd, storagecostsusd, personnelcostsusd, fundingstate, donorcommitmentsusd, resourcegapsusd. Joins to disasterevents, operations.'
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_schema.txt
  title: disaster schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_column_meaning_base.json
  title: disaster column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `financeregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each financial record (e.g., 'FIN0001'). |
| `findistref` | character varying | A VARCHAR(20) referencing DisasterEvents(DistRegistry), tying finances to a specific event (e.g., 'DIST0001'). |
| `finopsref` | character varying | A VARCHAR(20) referencing Operations(OpsRegistry), linking finances to operations (e.g., 'OPS0001'). |
| `budgetallotusd` | numeric | A DECIMAL(16,3) for the allocated budget in USD (e.g., 1000000.000). |
| `fundsutilpct` | numeric | A DECIMAL(7,3) measuring percentage of utilized funds (e.g., 75.500). |
| `costbeneusd` | numeric | A NUMERIC(14,3) capturing the cost per beneficiary in USD (e.g., 15.250). |
| `opscostsusd` | numeric | A DECIMAL(15,2) describing total operational costs (e.g., 350000.00). |
| `transportcostsusd` | integer | An INT representing transportation costs (e.g., 15000). |
| `storagecostsusd` | numeric | A NUMERIC(13,3) detailing storage costs (e.g., 8000.000). |
| `personnelcostsusd` | numeric | A DECIMAL(15,4) enumerating personnel costs in USD (e.g., 50000.0000). |
| `fundingstate` | USER-DEFINED | An enum (FundingState_enum) labeling funding status; values: 'Critical', 'Adequate', 'Limited'. |
| `donorcommitmentsusd` | numeric | A DECIMAL(14,2) representing pledged donor funds (e.g., 200000.00). |
| `resourcegapsusd` | integer | An INT recording the gap in resources needed (e.g., 50000). |

# Joins

* `findistref` references `distregistry` in [disasterevents](/tables/disasterevents.md).
* `finopsref` references `opsregistry` in [operations](/tables/operations.md).

# Related knowledge

* [fundingstate](/knowledge/fundingstate.md)
* [Personnel Effectiveness Ratio (PER)](/knowledge/personnel-effectiveness-ratio.md)
* [Financial Sustainability Ratio (FSR)](/knowledge/financial-sustainability-ratio.md)
* [Financial Crisis Risk](/knowledge/financial-crisis-risk.md)
* [Financial Efficiency Metric (FEM)](/knowledge/financial-efficiency-metric.md)
