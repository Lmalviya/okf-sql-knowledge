---
type: Calculation
title: Encoding Complexity Index (ECI)
description: Evaluates the sophistication of potential encoding in the signal.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 6
---

# Definition

$\text{ECI} = \frac{\text{CompressRatio} \times \text{ComplexIdx} \times \text{EntropyVal}}{10}$, where values above 1.5 suggest deliberate information encoding rather than random patterns.

# Columns used

* [signalclassification](/tables/signalclassification.md): `complexidx`, `entropyval`
* [signaldecoding](/tables/signaldecoding.md): `compressratio`

# Used by

* [Encoded Information Transfer (EIT)](/knowledge/encoded-information-transfer.md)
* [Artificial Intelligence Detection Probability (AIDP)](/knowledge/artificial-intelligence-detection-probability.md)
* [Signal Processing Efficiency Index (SPEI)](/knowledge/signal-processing-efficiency-index.md)
* [Multi-Channel Communication Protocol](/knowledge/multi-channel-communication-protocol.md)
* [Quantum-Coherent Transmission](/knowledge/quantum-coherent-transmission.md)
