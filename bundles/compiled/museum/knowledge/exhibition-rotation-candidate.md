---
type: Business Rule
title: Exhibition Rotation Candidate
description: Identifies artifacts that should be considered for rotation out of display.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 15
---

# Definition

An artifact is a rotation candidate when its current display duration exceeds 75% of its DSD OR LER > 7.

# Depends on

* [Display Safety Duration (DSD)](/knowledge/display-safety-duration.md)
* [Light Exposure Risk (LER)](/knowledge/light-exposure-risk.md)

# Used by

* [Exhibition Rotation Urgency](/knowledge/exhibition-rotation-urgency.md)
