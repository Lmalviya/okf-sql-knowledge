---
type: Value Illustration
title: Sensitivity Weight Values
description: Numerical weights for sensitivity calculations
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 1
---

# Definition

EnvSensitivity: Low=1, Medium=5, High=10; LightSensitivity: Low=1, Medium=5, High=10; TempSensitivity: Low=1, Medium=5, High=10; HumiditySensitivity: Low=1, Medium=5, High=10

# Columns used

* [sensitivitydata](/tables/sensitivitydata.md): `envsensitivity`, `lightsensitivity`, `tempsensitivity`, `humiditysensitivity`

# Used by

* [Environmental Risk Factor (ERF)](/knowledge/environmental-risk-factor.md)
* [Display Safety Duration (DSD)](/knowledge/display-safety-duration.md)
* [Light Exposure Risk (LER)](/knowledge/light-exposure-risk.md)
