---
type: Calculation
title: Input Responsiveness Score (IRS)
description: Quantifies the overall input responsiveness of a device considering polling rate, latency, and response time.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 2
---

# Definition

IRS = \frac{PollRateHz}{100} \times \left(1 - \frac{InpLagMs + RespTimeMs}{30}\right) \times 10, \text{ where higher values indicate more responsive input with minimal lag.}

# Columns used

* [testsessions](/tables/testsessions.md): `inplagms`, `pollratehz`, `resptimems`

# Used by

* [Gaming Device Value Index (GDVI)](/knowledge/gaming-device-value-index.md)
* [Tournament-Ready Keyboard](/knowledge/tournament-ready-keyboard.md)
* [Professional Esports Controller](/knowledge/professional-esports-controller.md)
* [Competitive Gaming Performance Index (CGPI)](/knowledge/competitive-gaming-performance-index.md)
* [Professional Adoption Rating (PAR)](/knowledge/professional-adoption-rating.md)
* [Ultra-Responsive Gaming Device](/knowledge/ultra-responsive-gaming-device.md)
