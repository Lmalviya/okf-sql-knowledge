---
type: Business Rule
title: Regulatory Overload Flow
description: Highlights data flows with both regulatory risk and compliance gaps.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 46
---

# Definition

A data flow with Regulatory Risk Exposure and GdprComp = 'Non-compliant'

# Columns used

* [compliance](/tables/compliance.md): `gdprcomp`

# Depends on

* [Regulatory Risk Exposure](/knowledge/regulatory-risk-exposure.md)
* [Compliance.GdprComp](/knowledge/compliance-gdprcomp.md)
