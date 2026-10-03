---
type: Value Illustration
title: AuditAndCompliance.RespTimeDay
description: Illustrates the response time for data subject requests.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 26
---

# Definition

Ranges from 0 to days. A RespTimeDay of 1.5 suggests quick responses, while >7 indicates delays, from AuditAndCompliance.

# Columns used

* [auditandcompliance](/tables/auditandcompliance.md): `resptimeday`

# Used by

* [Data Subject Request Pressure (DSRP)](/knowledge/data-subject-request-pressure.md)
