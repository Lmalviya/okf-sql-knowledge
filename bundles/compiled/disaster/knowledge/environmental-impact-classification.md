---
type: Business Rule
title: Environmental Impact Classification
description: Categorizes operations based on their Environmental Impact Factor (EIF) values
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 51
---

# Definition

Sustainable (EIF < 50) indicates operations with minimal environmental footprint and strong sustainability practices; Moderate Impact (50 ≤ EIF < 100) represents operations with reasonable environmental management; High Impact (EIF ≥ 100) indicates operations with significant environmental footprint requiring mitigation strategies

# Depends on

* [Environmental Impact Factor (EIF)](/knowledge/environmental-impact-factor.md)
