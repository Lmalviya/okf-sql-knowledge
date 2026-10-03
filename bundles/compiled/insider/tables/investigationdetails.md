---
type: PostgreSQL Table
title: investigationdetails
description: '18 columns: reginv, patrecsc, behansc, netansc, relmapstat, connent, commaddr, sharectc, finrel, commpat, tcirclesz, grpbehsc, mktabprob, evidstr, docustat. Joins to compliancecase, sentimentandfundamentals.'
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_schema.txt
  title: insider schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_column_meaning_base.json
  title: insider column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `invdetreg` | character varying, primary key | VARCHAR(50). Primary key for a detailed investigation record. |
| `compref` | character varying | VARCHAR(50). Foreign‑key to ComplianceCase.CompReg that the investigation expands upon. |
| `reginv` | USER-DEFINED | regulatory_investigation_enum (enum: 'Preliminary', 'Active'). Current phase of regulatory investigation. |
| `patrecsc` | numeric | NUMERIC(7,4). Pattern‑recognition match score (e.g., 0.8045). |
| `behansc` | numeric | NUMERIC(7,4). Behavioural analysis score (e.g., 0.6230). |
| `netansc` | numeric | NUMERIC(7,4). Network‑analysis anomaly score (e.g., 0.4156). |
| `relmapstat` | USER-DEFINED | relationship_mapping_status_enum (enum: 'Pending', 'Partial', 'Complete'). Status of mapping relationships among entities. |
| `connent` | character varying | VARCHAR(100). List or description of connected entities uncovered. |
| `commaddr` | integer | INT. Count of shared physical or IP addresses across the network (e.g., 3). |
| `sharectc` | USER-DEFINED | shared_contact_info_enum (enum: 'Email', 'Phone', 'Multiple'). Type of shared contact information identified. |
| `finrel` | USER-DEFINED | financial_relationship_enum (enum: 'Business', 'Personal'). Nature of financial relationships linked. |
| `commpat` | USER-DEFINED | communication_pattern_enum (enum: 'Regular', 'Irregular'). Observed communication pattern among parties. |
| `tcirclesz` | integer | INT. Size of the trading circle or colluding group (e.g., 6). |
| `grpbehsc` | numeric | NUMERIC(7,4). Group‑behaviour risk score (e.g., 0.5678). |
| `mktabprob` | numeric | NUMERIC(5,2). Estimated probability of market‑abuse activity (e.g., 22.60). |
| `evidstr` | USER-DEFINED | evidence_strength_enum (enum: 'Weak', 'Moderate', 'Strong'). Strength of supporting evidence. |
| `docustat` | USER-DEFINED | documentation_status_enum (enum: 'Incomplete', 'Partial', 'Complete'). Documentation completeness level. |
| `sentref` | character varying | VARCHAR(50). Optional foreign‑key to SentimentAndFundamentals.SentReg for sentiment context. |

# Joins

* `compref` references `compreg` in [compliancecase](/tables/compliancecase.md).
* `sentref` references `sentreg` in [sentimentandfundamentals](/tables/sentimentandfundamentals.md).

# Related knowledge

* [Investigation Intensity Index (III)](/knowledge/investigation-intensity-index.md)
* [Collusion Network Indicator](/knowledge/collusion-network-indicator.md)
