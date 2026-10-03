---
type: Value Illustration
title: SensitivityData.LightSensitivity
description: Illustrates light sensitivity classifications and their implications.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 23
---

# Definition

Values include 'Low' (can tolerate up to 300 lux, like stone artifacts), 'Medium' (should be limited to 150-200 lux, like oil paintings), and 'High' (restricted to 50 lux or less, like textiles and works on paper).

# Columns used

* [sensitivitydata](/tables/sensitivitydata.md): `lightsensitivity`
