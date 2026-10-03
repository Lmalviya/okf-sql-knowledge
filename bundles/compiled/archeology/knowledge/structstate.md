---
type: Value Illustration
title: StructState (Structural State)
description: Illustrates structural state classifications in archaeological conservation.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 26
---

# Definition

A categorical assessment with specific values: 'Stable' indicates structures that maintain integrity under normal conditions, 'Unstable' indicates structures showing signs of deterioration requiring intervention, and 'Critical' indicates structures at imminent risk of collapse requiring emergency stabilization.

# Columns used

* [scanconservation](/tables/scanconservation.md): `structstate`

# Used by

* [Degradation Risk Zone](/knowledge/degradation-risk-zone.md)
* [Risk Zone Category](/knowledge/risk-zone-category.md)
