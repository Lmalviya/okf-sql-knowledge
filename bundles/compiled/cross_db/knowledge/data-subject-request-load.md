---
type: Calculation
title: Data Subject Request Load (DSRL)
description: Measures the workload from data subject requests.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 8
---

# Definition

DSRL = \text{AccReqNum} + \text{DelReqNum} + \text{RectReqNum} + \text{PortReqNum}

# Columns used

* [auditandcompliance](/tables/auditandcompliance.md): `accreqnum`, `delreqnum`, `rectreqnum`, `portreqnum`

# Used by

* [Data Subject Request Pressure (DSRP)](/knowledge/data-subject-request-pressure.md)
* [Audit Remediation Load (ARL)](/knowledge/audit-remediation-load.md)
