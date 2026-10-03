---
type: Business Rule
title: Subpar Audio Device Identification
description: Identifies audio devices that fail to meet audiophile gaming standards and need improvement or removal from premium product lines
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 52
---

# Definition

Audio devices with one or more critical quality deficiencies: AQI score of 8.0 or lower, total harmonic distortion (ThdPct) of 0.5% or higher, noise isolation (NoiseIsoDb) of 15dB or lower, or frequency response not covering the full 10Hz-22kHz range required for immersive gaming audio experiences. These devices are candidates for improvement or reclassification to non-audiophile product categories.

# Columns used

* [audioandmedia](/tables/audioandmedia.md): `noiseisodb`, `thdpct`

# Depends on

* [Audio Quality Index (AQI)](/knowledge/audio-quality-index.md)
* [Audiophile Gaming Headset](/knowledge/audiophile-gaming-headset.md)
