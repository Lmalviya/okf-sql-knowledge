---
type: Calculation
title: Modulation Complexity Score (MCS)
description: Quantifies the sophistication of signal modulation based on type and stability.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 30
---

# Definition

$\text{MCS} = \text{ModIndex} \times (1 + \text{SSM}) \times M_{\text{factor}}$, where $M_{\text{factor}}$ is 2 for $\text{ModType} = \text{'AM'}$, 1.5 for 'FM', and 1 for other types. Incorporates Signal Stability Metric (SSM) to weight stable modulations higher.

# Columns used

* [signals](/tables/signals.md): `modtype`, `modindex`

# Depends on

* [Signal Stability Metric (SSM)](/knowledge/signal-stability-metric.md)

# Used by

* [High-Confidence Technosignature](/knowledge/high-confidence-technosignature.md)
* [Anomalous Quantum Signal](/knowledge/anomalous-quantum-signal.md)
