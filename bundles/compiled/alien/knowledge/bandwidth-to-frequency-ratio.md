---
type: Calculation
title: Bandwidth-to-Frequency Ratio (BFR)
description: Normalized signal width relative to its central frequency.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 51
---

# Definition

$\text{BFR} = \frac{\text{BwHz}}{\text{CenterFreqMhz} \times 1{,}000{,}000}$, used to characterize signal spread relative to its frequency band.

# Columns used

* [signals](/tables/signals.md): `bwhz`, `centerfreqmhz`
