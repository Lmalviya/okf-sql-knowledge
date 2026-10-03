---
type: Business Rule
title: Professional Esports Controller
description: Defines the quality standards for controllers used in professional esports competitions.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 14
---

# Definition

A controller with IRS > 8.0, JoyPrec > 9.0, DriftRes > 9.5, TrigRes ≥ 5, and HapStr > 8, offering precise inputs and reliable performance required for competitive play at the highest level.

# Columns used

* [interactionandcontrol](/tables/interactionandcontrol.md): `hapstr`, `trigres`, `joyprec`, `driftres`

# Depends on

* [Input Responsiveness Score (IRS)](/knowledge/input-responsiveness-score.md)
