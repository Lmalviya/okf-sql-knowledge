---
type: Business Rule
title: NTM Classification System
description: A tiered classification system for Narrowband Technological Markers based on signal characteristics.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 39
---

# Definition

Three-tier classification: 'Strong NTM' (BFR < 0.0001 AND FreqDriftHzs < 0.1 AND non-natural modulation), 'Moderate NTM' (BFR < 0.0005 AND FreqDriftHzs < 0.5 AND non-natural modulation), and 'Not NTM' (all other signals).

# Columns used

* [signals](/tables/signals.md): `freqdrifthzs`

# Depends on

* [Narrowband Technological Marker (NTM)](/knowledge/narrowband-technological-marker.md)
* [Bandwidth-Frequency Ratio (BFR)](/knowledge/bandwidth-frequency-ratio.md)

# Used by

* [Research Critical Signal](/knowledge/research-critical-signal.md)
