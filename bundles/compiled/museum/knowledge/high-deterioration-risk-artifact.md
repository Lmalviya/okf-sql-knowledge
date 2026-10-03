---
type: Business Rule
title: High Deterioration Risk Artifact
description: Identifies artifacts at high risk of rapid deterioration due to environmental factors.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 42
---

# Definition

An artifact that has TETL > 15 AND falls under the Accelerated Deterioration Scenario.

# Depends on

* [Total Environmental Threat Level (TETL)](/knowledge/total-environmental-threat-level.md)
* [Accelerated Deterioration Scenario](/knowledge/accelerated-deterioration-scenario.md)
