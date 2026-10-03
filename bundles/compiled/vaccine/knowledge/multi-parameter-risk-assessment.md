---
type: Calculation
title: Multi-Parameter Risk Assessment (MPRA)
description: Comprehensive risk evaluation using multiple environmental parameters.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 51
---

# Definition

MPRA = \sqrt{\text{CRI}^2 + \text{TBS}^2 + (1-\text{HQI})^2} \times (1 + \frac{\text{CDR}}{\text{CDR}_{\text{max}}})

# Depends on

* [Container Risk Index (CRI)](/knowledge/container-risk-index.md)
* [Temperature Breach Severity (TBS)](/knowledge/temperature-breach-severity.md)
* [Handling Quality Index (HQI)](/knowledge/handling-quality-index.md)
* [Coolant Depletion Rate (CDR)](/knowledge/coolant-depletion-rate.md)

# Used by

* [Critical Cascade Condition](/knowledge/critical-cascade-condition.md)
* [Dynamic Stability Threshold](/knowledge/dynamic-stability-threshold.md)
