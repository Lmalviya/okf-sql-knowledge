---
type: Value Illustration
title: CumDegPct (Cumulative Degradation Percentage)
description: Illustrates the total performance loss over a panel's lifetime.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 27
---

# Definition

Expressed as a percentage, representing total performance degradation since installation. New panels start at 0%, while panels approaching end-of-life may have values of 15-20% or higher, with manufacturer warranties typically covering degradation up to 20% over 25 years.

# Used by

* [Total System Loss (TSL)](/knowledge/total-system-loss.md)
