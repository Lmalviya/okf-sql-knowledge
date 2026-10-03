---
type: Value Illustration
title: SensitivityData.HumiditySensitivity
description: Illustrates humidity sensitivity classifications and their implications.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 24
---

# Definition

Values include 'Low' (can tolerate 30-65% RH, like stone artifacts), 'Medium' (requires 40-60% RH, like wood), and 'High' (requires 45-55% RH with minimal fluctuation, like lacquer work).

# Columns used

* [sensitivitydata](/tables/sensitivitydata.md): `humiditysensitivity`
