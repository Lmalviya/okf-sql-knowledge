---
type: Business Rule
title: Analyzable Signals
description: Signals of sufficient quality to be considered useful for further analysis.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 50
---

# Definition

Signals with SNQI > 0 are considered analyzable.

# Depends on

* [Signal-to-Noise Quality Indicator (SNQI)](/knowledge/signal-to-noise-quality-indicator.md)
