---
type: Business Rule
title: Exhibition Rotation Urgency
description: Identifies artifacts that should be immediately removed from exhibition.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 43
---

# Definition

Occurs when an artifact is an Exhibition Rotation Candidate AND has an ERPS < 0.

# Depends on

* [Exhibition Rotation Candidate](/knowledge/exhibition-rotation-candidate.md)
* [Exhibition Rotation Priority Score (ERPS)](/knowledge/exhibition-rotation-priority-score.md)
