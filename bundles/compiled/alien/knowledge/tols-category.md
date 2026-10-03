---
type: Business Rule
title: TOLS Category
description: Classification of signals based on TOLS thresholds.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 52
---

# Definition

Categorized as 'Low' if TOLS < 0.25, 'Medium' if TOLS < 0.75, and 'High' otherwise.

# Depends on

* [Technological Origin Likelihood Score (TOLS)](/knowledge/technological-origin-likelihood-score.md)
