---
type: Calculation
title: Signal Stability Metric (SSM)
description: Quantifies overall temporal and spectral stability of a signal.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 7
---

# Definition

$\text{SSM} = (1 - \frac{|\text{FreqDriftHzs}|}{\text{FreqMhz} \times 1000}) \times \frac{\text{SigDurSec}}{1 + \frac{\text{DoppShiftHz}}{1000}}$, where higher values indicate more stable signals typical of fixed transmitters.

# Columns used

* [signals](/tables/signals.md): `freqmhz`, `freqdrifthzs`, `doppshifthz`, `sigdursec`

# Used by

* [Coherent Information Pattern (CIP)](/knowledge/coherent-information-pattern.md)
* [CIP Classification Label](/knowledge/cip-classification-label.md)
* [Modulation Complexity Score (MCS)](/knowledge/modulation-complexity-score.md)
