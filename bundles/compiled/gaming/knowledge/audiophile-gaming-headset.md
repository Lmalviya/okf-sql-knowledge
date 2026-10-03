---
type: Business Rule
title: Audiophile Gaming Headset
description: Defines the standards for premium audio quality in gaming headsets suitable for audiophiles.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 12
---

# Definition

A headset with AQI > 8.0, FreqResp covering at least '10Hz-22kHz', ThdPct < 0.5%, and NoiseIsoDb > 15, delivering exceptional sound clarity, detail, and isolation for immersive gaming experiences.

# Columns used

* [audioandmedia](/tables/audioandmedia.md): `noiseisodb`, `thdpct`, `freqresp`

# Depends on

* [Audio Quality Index (AQI)](/knowledge/audio-quality-index.md)

# Used by

* [Subpar Audio Device Identification](/knowledge/subpar-audio-device-identification.md)
