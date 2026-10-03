---
type: Business Rule
title: End-of-Life Indicator
description: Defines criteria for determining when a panel should be considered for replacement.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 14
---

# Definition

A panel has reached effective end-of-life when its cumulative degradation exceeds 20% or when maintenance costs in a 12-month period exceed 30% of replacement value.
