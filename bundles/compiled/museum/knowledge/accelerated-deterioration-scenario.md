---
type: Business Rule
title: Accelerated Deterioration Scenario
description: Identifies conditions that could lead to rapid artifact deterioration.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 14
---

# Definition

Occurs when MDR > 5 AND at least two SensitivityData values are 'High'.

# Depends on

* [Material Deterioration Rate (MDR)](/knowledge/material-deterioration-rate.md)

# Used by

* [High Deterioration Risk Artifact](/knowledge/high-deterioration-risk-artifact.md)
