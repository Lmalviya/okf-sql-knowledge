---
type: Business Rule
title: Grid Export Quality Classification
description: Classification system for the quality of power exported to the grid.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 45
---

# Definition

Power export quality is classified as 'Premium' when Grid Integration Quality exceeds 0.95, 'Standard' when between 0.90 and 0.95, and 'Substandard' when below 0.90, with substandard exports potentially subject to utility penalties.

# Depends on

* [Grid Integration Quality (GIQ)](/knowledge/grid-integration-quality.md)
