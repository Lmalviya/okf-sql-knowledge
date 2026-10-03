---
type: PostgreSQL Table
title: dataprofile
description: '15 columns: recordregistry, datatype, datasense, volgb, rectally, subjtally, retdays, formattype, qltyscore, intcheck, csumverify, srcvalstate, destvalstate. Joins to dataflow, riskmanagement.'
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_schema.txt
  title: cross_db schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_column_meaning_base.json
  title: cross_db column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `flowsign` | character | CHAR(10) referencing DataFlow(RecordRegistry), linking this profile to a particular data flow. |
| `riskjoin` | integer | INT referencing RiskManagement(RiskTrace). Associates the data profile with a relevant risk record. |
| `recordregistry` | character | CHAR(10), an optional cross-reference, formerly 'RecordID'. |
| `datatype` | character varying | VARCHAR(80) describing the category of data (financial, personal, logs, etc.). Currently possible values: (Commercial, Personal, Financial, Industrial, Medical). |
| `datasense` | character varying | VARCHAR(30) designating data sensitivity level (High, Medium, Low). Currently possible values: (High, Low, Critical, Medium). |
| `volgb` | numeric | NUMERIC(10,2) representing the approximate data volume in gigabytes. |
| `rectally` | bigint | BIGINT counting how many records exist in this data set or flow. |
| `subjtally` | bigint | BIGINT enumerating how many unique data subjects are impacted/contained. |
| `retdays` | integer | INT storing the retention duration (in days) for this data. |
| `formattype` | character varying | VARCHAR(80) naming the data format (CSV, JSON, XML, proprietary, etc.). Currently possible values: (Mixed, Unstructured, Structured). |
| `qltyscore` | numeric | NUMERIC(4,2) capturing data quality on a custom 0–100 scale. |
| `intcheck` | USER-DEFINED | checkstatus_enum enumerating data integrity check status. Currently possible values: (Passed, Failed, Partial). |
| `csumverify` | USER-DEFINED | checkstatus_enum enumerating checksum verification status. Currently possible values: (Failed, Success, Pending). |
| `srcvalstate` | USER-DEFINED | checkstatus_enum enumerating source validation status. Currently possible values: (Pending, Verified, Failed). |
| `destvalstate` | USER-DEFINED | checkstatus_enum enumerating destination validation status. Currently possible values: (Pending, Verified, Failed). |

# Joins

* `flowsign` references `recordregistry` in [dataflow](/tables/dataflow.md).
* `riskjoin` references `risktrace` in [riskmanagement](/tables/riskmanagement.md).

# Related knowledge

* [Data Sensitivity Index (DSI)](/knowledge/data-sensitivity-index.md)
* [Data Integrity Failure](/knowledge/data-integrity-failure.md)
* [DataProfile.VolGB](/knowledge/dataprofile-volgb.md)
* [Cross-Border Data Volume Risk (CDVR)](/knowledge/cross-border-data-volume-risk.md)
* [Insecure High-Volume Flow](/knowledge/insecure-high-volume-flow.md)
* [Data Retention Risk Score (DRRS)](/knowledge/data-retention-risk-score.md)
* [Integrity Failure Count (IFC)](/knowledge/integrity-failure-count.md)
* [Failure Types List](/knowledge/failure-types-list.md)
