---
type: Business Rule
title: Severe Container Risk
description: Identifies containers with severe combined risks.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 41
---

# Definition

A container where CES < 0.3 and CEI < 0.5

# Depends on

* [Container Efficiency Score (CES)](/knowledge/container-efficiency-score.md)
* [Coolant Efficiency Index (CEI)](/knowledge/coolant-efficiency-index.md)
