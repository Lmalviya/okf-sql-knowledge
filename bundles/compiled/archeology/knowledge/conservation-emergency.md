---
type: Business Rule
title: Conservation Emergency
description: Identifies sites requiring immediate conservation intervention based on multiple risk factors and structural assessment.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 42
---

# Definition

A site that is in a Degradation Risk Zone with CPI > 75, where CPI is the Conservation Priority Index, requiring immediate protective measures and priority documentation with at least Premium Quality Scans before any intervention to establish baseline condition.

# Depends on

* [Degradation Risk Zone](/knowledge/degradation-risk-zone.md)
* [Conservation Priority Index (CPI)](/knowledge/conservation-priority-index.md)
