---
type: Calculation
title: Energy Production Efficiency (EPE)
description: Measures the overall energy production efficiency considering all losses.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 3
---

# Definition

EPE = PPR \times (1 - SoilingLossPercent/100) \times (1 - CumulativeDegradationPercent/100), \text{where PPR is the Panel Performance Ratio.}

# Depends on

* [Panel Performance Ratio (PPR)](/knowledge/panel-performance-ratio.md)

# Used by

* [Warranty Claim Threshold](/knowledge/warranty-claim-threshold.md)
* [Expected Energy Yield (EEY)](/knowledge/expected-energy-yield.md)
* [Premium Maintenance Candidate](/knowledge/premium-maintenance-candidate.md)
