---
type: Business Rule
title: Narrowband Technological Marker (NTM)
description: Identifies a specific signature associated with technological transmission.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 15
---

# Definition

Signals with extremely narrow bandwidth ($\text{BFR} < 0.0001$), stable frequency ($\text{FreqDriftHzs} < 0.1$).

# Columns used

* [signals](/tables/signals.md): `freqdrifthzs`

# Depends on

* [Bandwidth-Frequency Ratio (BFR)](/knowledge/bandwidth-frequency-ratio.md)

# Used by

* [NTM Classification System](/knowledge/ntm-classification-system.md)
