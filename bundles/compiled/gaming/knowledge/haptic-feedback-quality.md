---
type: Calculation
title: Haptic Feedback Quality (HFQ)
description: Measures the quality and effectiveness of haptic feedback systems in gaming controllers and devices.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 34
---

# Definition

HFQ = \left(\frac{HapStr}{10}\right) \times \left(1 + \frac{VibModes}{10}\right) \times \left(1 + \frac{ForceFeed\_length}{20}\right)

# Columns used

* [interactionandcontrol](/tables/interactionandcontrol.md): `hapstr`, `vibmodes`, `forcefeed`

# Used by

* [Immersion Enhancement Coefficient (IEC)](/knowledge/immersion-enhancement-coefficient.md)
* [Premium Immersive Experience Device](/knowledge/premium-immersive-experience-device.md)
