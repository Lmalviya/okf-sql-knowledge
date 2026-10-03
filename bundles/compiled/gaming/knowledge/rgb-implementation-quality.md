---
type: Calculation
title: RGB Implementation Quality (RIQ)
description: Evaluates the quality of RGB implementation based on brightness, color accuracy, and lighting zones.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 6
---

# Definition

RIQ = \frac{RgbBright}{100} \times \frac{RgbColorAcc}{10} \times \left(0.5 + \frac{RgbZones}{20}\right), \text{ where higher values indicate premium RGB lighting with accurate colors and extensive customization options.}

# Columns used

* [rgb](/tables/rgb.md): `rgbbright`, `rgbcoloracc`, `rgbzones`

# Used by

* [Immersion Enhancement Coefficient (IEC)](/knowledge/immersion-enhancement-coefficient.md)
* [Premium Immersive Experience Device](/knowledge/premium-immersive-experience-device.md)
* [RGB Quality Classification](/knowledge/rgb-quality-classification.md)
