---
type: Calculation
title: Normalized Degradation Index (NDI)
description: Compares panel degradation to expected rates based on panel type and age.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 34
---

# Definition

NDI = PELR / AnnDegRate, where PELR is the Panel Efficiency Loss Rate and AnnDegRate is from efficiency_profile.degradation.anndegrate. Values above 1.0 indicate faster than expected degradation.

# Columns used

* [performance](/tables/performance.md): `efficiency_profile`

# Depends on

* [Panel Efficiency Loss Rate (PELR)](/knowledge/panel-efficiency-loss-rate.md)
* [AnnDegRate (Annual Degradation Rate)](/knowledge/anndegrate.md)

# Used by

* [Financial Impact of Degradation (FID)](/knowledge/financial-impact-of-degradation.md)
* [Advanced Performance Degradation Alert](/knowledge/advanced-performance-degradation-alert.md)
* [End-of-Warranty Optimization](/knowledge/end-of-warranty-optimization.md)
* [Degradation Severity Classification](/knowledge/degradation-severity-classification.md)
