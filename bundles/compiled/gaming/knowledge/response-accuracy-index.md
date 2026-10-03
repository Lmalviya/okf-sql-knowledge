---
type: Calculation
title: Response Accuracy Index (RAI)
description: Measures the accuracy and consistency of input response in gaming devices, accounting for both sensor precision and control stability.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 31
---

# Definition

RAI = \left(\frac{JoyPrec + DpadAcc}{20}\right) \times \left(1 - \frac{InpLagMs}{10}\right) \times 10

# Columns used

* [testsessions](/tables/testsessions.md): `inplagms`
* [interactionandcontrol](/tables/interactionandcontrol.md): `joyprec`, `dpadacc`

# Used by

* [Competitive Gaming Performance Index (CGPI)](/knowledge/competitive-gaming-performance-index.md)
* [Ultra-Responsive Gaming Device](/knowledge/ultra-responsive-gaming-device.md)
* [Professional-Grade Control Consistency](/knowledge/professional-grade-control-consistency.md)
