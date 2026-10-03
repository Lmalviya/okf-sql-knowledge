---
type: PostgreSQL Table
title: dataflow
description: '15 columns: flowstamp, flowtag, orignation, destnation, origactor, destactor, chanproto, chanfreq, datasizemb, durmin, bwidthpct, successpct, errtally, rtrytally.'
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
| `recordregistry` | character, primary key | CHAR(10) primary key uniquely identifying each data flow record in the DataFlow table. |
| `flowstamp` | timestamp without time zone | TIMESTAMP(6) for the moment this data flow record was created or logged. Microsecond precision. |
| `flowtag` | character varying | A short identifier or tag (VARCHAR(20)) for the data flow, previously 'DataFlowID'. |
| `orignation` | character varying | VARCHAR(80) storing the source/origin country's name for this data flow. |
| `destnation` | character varying | VARCHAR(80) storing the destination country's name for this data flow. |
| `origactor` | character varying | VARCHAR(150) referencing the source entity/system initiating the flow (person, organization, or app). |
| `destactor` | character varying | VARCHAR(150) referencing the destination entity/system receiving the flow. |
| `chanproto` | character varying | VARCHAR(30) for the protocol used (HTTP, FTP, SFTP, etc.). Currently possible values: (Blockchain, SFTP, Private Network, HTTPS). |
| `chanfreq` | character varying | VARCHAR(25) specifying how frequently data is transferred (daily, weekly, on-demand, etc.). Currently possible values: (Weekly, Hourly, Real-time, Daily). |
| `datasizemb` | numeric | NUMERIC(12,2) representing the size in MB of each data transfer. |
| `durmin` | smallint | SMALLINT capturing the average or actual duration (in minutes) of the data flow. |
| `bwidthpct` | numeric | NUMERIC(5,2) for bandwidth utilization percentage (0 to 100%). |
| `successpct` | numeric | NUMERIC(5,2) measuring the success rate (0–100%) of the flow attempts. |
| `errtally` | smallint | SMALLINT counting the total errors or failures observed for this data flow. |
| `rtrytally` | smallint | SMALLINT storing how many retry attempts were made after failures. |

# Related knowledge

* [Data Transfer Efficiency (DTE)](/knowledge/data-transfer-efficiency.md)
* [Bandwidth Saturation Index (BSI)](/knowledge/bandwidth-saturation-index.md)
* [Cross-Border Risk Factor (CBRF)](/knowledge/cross-border-risk-factor.md)
* [Cross-Border Compliance Gap](/knowledge/cross-border-compliance-gap.md)
* [DataFlow.SuccessPct](/knowledge/dataflow-successpct.md)
* [DataFlow.ErrTally](/knowledge/dataflow-errtally.md)
* [Data Flow Reliability Score (DFRS)](/knowledge/data-flow-reliability-score.md)
* [Data Flow Stability Index (DFSI)](/knowledge/data-flow-stability-index.md)
* [Transfer Path](/knowledge/transfer-path.md)
* [Cross-Border Data Flow](/knowledge/cross-border-data-flow.md)
