---
type: Business Rule
title: High Confidence Signals
description: Signal with Confirmation Confidence Score (CCS) > 0.8, indicating high reliability.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 54
---

# Definition

Signals where $\text{CCS} > 0.8$

# Depends on

* [Confirmation Confidence Score (CCS)](/knowledge/confirmation-confidence-score.md)
