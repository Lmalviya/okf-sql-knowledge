---
type: Business Rule
title: High Temporal Value Site
description: Identifies sites with exceptional historical significance based on age and context for prioritized research attention.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 46
---

# Definition

A site with GuessDate containing dates before 500 CE and CPI > 60, where CPI is Conservation Priority Index, representing locations of exceptional chronological significance requiring specialized documentation protocols to capture temporally significant features.

# Columns used

* [sites](/tables/sites.md): `guessdate`

# Depends on

* [Conservation Priority Index (CPI)](/knowledge/conservation-priority-index.md)
* [GuessDate (Estimated Dating)](/knowledge/guessdate.md)
