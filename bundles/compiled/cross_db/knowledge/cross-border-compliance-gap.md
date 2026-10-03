---
type: Business Rule
title: Cross-Border Compliance Gap
description: Identifies compliance issues in cross-border data flows.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 15
---

# Definition

A compliance record where GdprComp = 'Non-compliant' or LocLawComp = 'Non-compliant' and OrigNation ≠ DestNation

# Columns used

* [dataflow](/tables/dataflow.md): `orignation`, `destnation`
* [compliance](/tables/compliance.md): `gdprcomp`, `loclawcomp`

# Used by

* [Regulatory Risk Exposure](/knowledge/regulatory-risk-exposure.md)
* [Bandwidth-Limited Compliance Risk](/knowledge/bandwidth-limited-compliance-risk.md)
