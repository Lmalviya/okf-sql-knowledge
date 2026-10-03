---
type: Business Rule
title: Visitor Crowd Risk
description: Identifies exhibition halls where high visitor numbers pose risks to artifact safety.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 19
---

# Definition

Occurs when VIR > 5 AND SecLevel='Level 1' for any artifact in the hall.

# Columns used

* [artifactsecurityaccess](/tables/artifactsecurityaccess.md): `seclevel`

# Depends on

* [Visitor Impact Risk (VIR)](/knowledge/visitor-impact-risk.md)

# Used by

* [Visitor Traffic Safety Concern](/knowledge/visitor-traffic-safety-concern.md)
