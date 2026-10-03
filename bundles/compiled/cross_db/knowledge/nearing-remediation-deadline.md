---
type: Business Rule
title: Nearing Remediation Deadline
description: Identifies data flows where the remediation deadline is within 5 days.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 77
---

# Definition

A data flow where (CURRENT_DATE - RemedDue) is between -5 and 0

# Columns used

* [auditandcompliance](/tables/auditandcompliance.md): `remeddue`
