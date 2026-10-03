---
type: Calculation
title: Overall Safety Performance Index (OSPI)
description: Comprehensively evaluates equipment's overall safety performance based on safety index and equipment efficiency rating
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 30
---

# Definition

OSPI = safetyindex × EER × 0.8

# Columns used

* [equipment](/tables/equipment.md): `safetyindex`

# Depends on

* [Equipment Efficiency Rating (EER)](/knowledge/equipment-efficiency-rating.md)

# Used by

* [Emergency Response Readiness Status (ERRS)](/knowledge/emergency-response-readiness-status.md)
* [Critical Infrastructure Protection Level (CIPL)](/knowledge/critical-infrastructure-protection-level.md)
