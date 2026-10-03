---
type: Calculation
title: Exhibition Rotation Priority Score (ERPS)
description: Calculates priority for rotating artifacts in and out of exhibition based on multiple factors.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 38
---

# Definition

ERPS = (DSD - DisplayDurMonths) × (LER + 1) × (CPI + 1) ÷ 100, where DSD is the Display Safety Duration, LER is the Light Exposure Risk, and CPI is the Conservation Priority Index. Lower values indicate higher rotation priority.

# Columns used

* [usagerecords](/tables/usagerecords.md): `displaydurmonths`

# Depends on

* [Display Safety Duration (DSD)](/knowledge/display-safety-duration.md)
* [Light Exposure Risk (LER)](/knowledge/light-exposure-risk.md)
* [Conservation Priority Index (CPI)](/knowledge/conservation-priority-index.md)

# Used by

* [Exhibition Rotation Urgency](/knowledge/exhibition-rotation-urgency.md)
* [ERPS Decision Threshold](/knowledge/erps-decision-threshold.md)
