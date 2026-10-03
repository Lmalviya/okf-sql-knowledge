---
type: Calculation
title: Logger Reliability Score (LRS)
description: Comprehensive score for logger reliability.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 34
---

# Definition

LRS = 	ext{LHI} \times (1 - \text{CMR}) \times \text{TSS}

# Depends on

* [Logger Health Index (LHI)](/knowledge/logger-health-index.md)
* [Combined Maintenance Risk (CMR)](/knowledge/combined-maintenance-risk.md)
* [Temperature Stability Score (TSS)](/knowledge/temperature-stability-score.md)

# Used by

* [Logger Critical State](/knowledge/logger-critical-state.md)
