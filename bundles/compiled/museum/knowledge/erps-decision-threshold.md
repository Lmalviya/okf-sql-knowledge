---
type: Business Rule
title: ERPS Decision Threshold
description: Converts ERPS scores into conservation actions
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 52
---

# Definition

When ERPS < 0, trigger 'Immediate Rotation'; otherwise 'Monitor'.

# Depends on

* [Exhibition Rotation Priority Score (ERPS)](/knowledge/exhibition-rotation-priority-score.md)
