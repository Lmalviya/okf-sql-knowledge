---
type: Business Rule
title: High Vendor Risk Concentration
description: Identifies vendors with elevated risk concentration based on vendor risk amplification and reliability.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 78
---

# Definition

A data flow where CURRENT_DATE - RemedDue > 0

# Columns used

* [auditandcompliance](/tables/auditandcompliance.md): `remeddue`
