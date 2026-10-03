---
type: Calculation
title: Immersion Enhancement Coefficient (IEC)
description: Quantifies how well a device contributes to gaming immersion through audio quality, haptic feedback, and visual elements.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 33
---

# Definition

IEC = \left(AQI \times 0.5\right) + \left(HFQ \times 0.3\right) + \left(RIQ \times 0.2\right)

# Depends on

* [Audio Quality Index (AQI)](/knowledge/audio-quality-index.md)
* [Haptic Feedback Quality (HFQ)](/knowledge/haptic-feedback-quality.md)
* [RGB Implementation Quality (RIQ)](/knowledge/rgb-implementation-quality.md)

# Used by

* [Gaming Versatility Score (GVS)](/knowledge/gaming-versatility-score.md)
* [Premium Immersive Experience Device](/knowledge/premium-immersive-experience-device.md)
