---
type: Business Rule
title: Incident-Prone Compliance Flow
description: Flags data flows with high incident impact and compliance gaps.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 64
---

# Definition

A data flow where IIF > 0.8 and GdprComp = 'Non-compliant'

# Columns used

* [compliance](/tables/compliance.md): `gdprcomp`

# Depends on

* [Compliance.GdprComp](/knowledge/compliance-gdprcomp.md)
* [Incident Impact Factor (IIF)](/knowledge/incident-impact-factor.md)
