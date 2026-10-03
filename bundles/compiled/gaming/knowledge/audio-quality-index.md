---
type: Calculation
title: Audio Quality Index (AQI)
description: A comprehensive metric for evaluating audio device quality based on frequency response, distortion, and sensitivity.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 4
---

# Definition

AQI = \left(1 - \frac{ThdPct}{2}\right) \times \frac{SpkSenseDb}{100} \times \left(1 - \frac{AudLatMs}{100}\right) \times 10, \text{ where higher values indicate better overall audio quality with minimal distortion.}

# Columns used

* [audioandmedia](/tables/audioandmedia.md): `audlatms`, `spksensedb`, `thdpct`

# Used by

* [Audiophile Gaming Headset](/knowledge/audiophile-gaming-headset.md)
* [Immersion Enhancement Coefficient (IEC)](/knowledge/immersion-enhancement-coefficient.md)
* [Premium Immersive Experience Device](/knowledge/premium-immersive-experience-device.md)
* [Subpar Audio Device Identification](/knowledge/subpar-audio-device-identification.md)
