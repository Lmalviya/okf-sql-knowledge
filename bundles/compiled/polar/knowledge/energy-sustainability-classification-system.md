---
type: Business Rule
title: Energy Sustainability Classification System (ESCS)
description: A comprehensive classification system that categorizes operational energy sustainability based on renewable energy contribution percentages.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 52
---

# Definition

Operations are classified into three sustainability levels: 'Energy-Sustainable' WHEN (REC > 70); 'Moderately Sustainable' WHEN (REC > 50 AND REC <= 70); 'Low Sustainability' WHEN (REC <= 50).

# Depends on

* [Renewable Energy Contribution (REC)](/knowledge/renewable-energy-contribution.md)
* [Sustainable Energy Operation](/knowledge/sustainable-energy-operation.md)
