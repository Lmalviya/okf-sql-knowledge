---
type: Calculation
title: Data Subject Request Pressure (DSRP)
description: Quantifies pressure from data subject requests relative to response time.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 34
---

# Definition

DSRP = \text{DSRL} \times \text{RespTimeDay}

# Columns used

* [auditandcompliance](/tables/auditandcompliance.md): `resptimeday`

# Depends on

* [Data Subject Request Load (DSRL)](/knowledge/data-subject-request-load.md)
* [AuditAndCompliance.RespTimeDay](/knowledge/auditandcompliance-resptimeday.md)

# Used by

* [High-Pressure Data Flow](/knowledge/high-pressure-data-flow.md)
* [Compliance Overhead Ratio (COR)](/knowledge/compliance-overhead-ratio.md)
