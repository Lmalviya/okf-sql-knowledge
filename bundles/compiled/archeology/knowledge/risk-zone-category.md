---
type: Business Rule
title: Risk Zone Category
description: Classification system that evaluates archaeological sites for degradation risk based on preservation status and structural condition.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 52
---

# Definition

Categorizes archaeological sites into two main groups: 'Degradation Risk Zone' and 'Not in Risk Zone'. 'Not in Risk Zone' means that the site is not in a Degradation Risk Zone.

# Depends on

* [Degradation Risk Zone](/knowledge/degradation-risk-zone.md)
* [StructState (Structural State)](/knowledge/structstate.md)
