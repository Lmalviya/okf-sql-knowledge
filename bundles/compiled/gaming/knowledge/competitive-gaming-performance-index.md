---
type: Calculation
title: Competitive Gaming Performance Index (CGPI)
description: A comprehensive metric evaluating a device's suitability for competitive gaming based on response time, accuracy, and durability.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 30
---

# Definition

CGPI = \left(IRS \times 0.4\right) + \left(SPI \times 0.3\right) + \left(SPR \times 0.2\right) + \left(RAI \times 0.1\right)

# Depends on

* [Input Responsiveness Score (IRS)](/knowledge/input-responsiveness-score.md)
* [Sensor Performance Index (SPI)](/knowledge/sensor-performance-index.md)
* [Switch Performance Rating (SPR)](/knowledge/switch-performance-rating.md)
* [Response Accuracy Index (RAI)](/knowledge/response-accuracy-index.md)

# Used by

* [Gaming Versatility Score (GVS)](/knowledge/gaming-versatility-score.md)
* [Professional Adoption Rating (PAR)](/knowledge/professional-adoption-rating.md)
* [Tournament Standard Device](/knowledge/tournament-standard-device.md)
* [Professional Multi-Genre Setup](/knowledge/professional-multi-genre-setup.md)
* [Pro-Player Performance Certified](/knowledge/pro-player-performance-certified.md)
