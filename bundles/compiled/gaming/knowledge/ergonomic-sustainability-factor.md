---
type: Calculation
title: Ergonomic Sustainability Factor (ESF)
description: Evaluates how suitable a device is for extended gaming sessions based on ergonomic design and comfort metrics.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 32
---

# Definition

ESF = CI \times \left(1 + \frac{ErgoRate - 5}{10}\right) \times \left(1 - \frac{|PalmAngle - 15|}{30}\right) \times \left(1 + \frac{ErgoRate \times WristFlag}{50}\right)

# Columns used

* [mechanical](/tables/mechanical.md): `wristflag`, `palmangle`, `ergorate`

# Depends on

* [Comfort Index (CI)](/knowledge/comfort-index.md)

# Used by

* [Value Proposition Index (VPI)](/knowledge/value-proposition-index.md)
* [Ergonomic Excellence Certification](/knowledge/ergonomic-excellence-certification.md)
