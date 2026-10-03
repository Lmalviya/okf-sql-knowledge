---
type: Calculation
title: Comfort Index (CI)
description: Evaluates the ergonomic comfort of a device based on its physical design factors and ergonomic rating.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 3
---

# Definition

CI = \frac{ErgoRate}{10} \times \left(1 + \frac{(WristFlag ? 1 : 0)}{5}\right) \times \left(1 - \frac{|PalmAngle - 15|}{45}\right) \times 10

# Columns used

* [mechanical](/tables/mechanical.md): `wristflag`, `palmangle`, `ergorate`

# Used by

* [Gaming Device Value Index (GDVI)](/knowledge/gaming-device-value-index.md)
* [Premium Gaming Mouse](/knowledge/premium-gaming-mouse.md)
* [Ergonomic Sustainability Factor (ESF)](/knowledge/ergonomic-sustainability-factor.md)
* [Ergonomic Excellence Certification](/knowledge/ergonomic-excellence-certification.md)
