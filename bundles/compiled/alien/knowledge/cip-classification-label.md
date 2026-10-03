---
type: Business Rule
title: CIP Classification Label
description: Three-tier rating system for evaluating signal coherence against intelligent transmission criteria.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 24
---

# Definition

Classification labels: 'Coherent Information Pattern Detected' ($\text{SSM} > 0.8$, $\text{EntropyVal}$ between 0.4-0.8, and $\text{ModIndex} > 0.5$), 'Potential Information Pattern' ($\text{SSM} > 0.6$ and $\text{EntropyVal}$ between 0.3-0.9$), or 'No Clear Pattern' (all other signals).

# Columns used

* [signals](/tables/signals.md): `modindex`
* [signalclassification](/tables/signalclassification.md): `entropyval`

# Depends on

* [Signal Stability Metric (SSM)](/knowledge/signal-stability-metric.md)
* [Coherent Information Pattern (CIP)](/knowledge/coherent-information-pattern.md)
