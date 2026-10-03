---
type: Business Rule
title: Premium Immersive Experience Device
description: Identifies devices specifically optimized to enhance gaming immersion through superior sensory feedback.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 44
---

# Definition

A device with IEC > 8.0, AQI > 7.5, HFQ > 8.0 if applicable, and RIQ > 7.0 if featuring lighting, designed to maximize player immersion in atmospheric and narrative-driven games.

# Depends on

* [Immersion Enhancement Coefficient (IEC)](/knowledge/immersion-enhancement-coefficient.md)
* [Audio Quality Index (AQI)](/knowledge/audio-quality-index.md)
* [Haptic Feedback Quality (HFQ)](/knowledge/haptic-feedback-quality.md)
* [RGB Implementation Quality (RIQ)](/knowledge/rgb-implementation-quality.md)
