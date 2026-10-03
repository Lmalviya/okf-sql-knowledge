---
type: Calculation
title: Switch Performance Rating (SPR)
description: Rates mechanical switch performance based on durability, consistency, and tactile feedback.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 5
---

# Definition

SPR = \frac{\log_{10}(SwtchDur)}{7} \times SwtchCons \times \left(1 - \frac{KeyChatter}{2}\right), \text{ where higher values indicate better switch quality with longer lifespan and consistent performance.}

# Columns used

* [mechanical](/tables/mechanical.md): `swtchdur`, `swtchcons`, `keychatter`

# Used by

* [Tournament-Ready Keyboard](/knowledge/tournament-ready-keyboard.md)
* [Competitive Gaming Performance Index (CGPI)](/knowledge/competitive-gaming-performance-index.md)
