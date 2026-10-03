---
type: Business Rule
title: Coherent Information Pattern (CIP)
description: Identifies signals showing patterns consistent with deliberate information transmission.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 11
---

# Definition

Signals characterized by high signal stability ($\text{SSM} > 0.8$), organized information structure ($\text{EntropyVal}$ between 0.4-0.8), and consistent modulation ($\text{ModType}$ with $\text{ModIndex} > 0.5$).

# Columns used

* [signals](/tables/signals.md): `modtype`, `modindex`
* [signalclassification](/tables/signalclassification.md): `entropyval`

# Depends on

* [Signal Stability Metric (SSM)](/knowledge/signal-stability-metric.md)

# Used by

* [CIP Classification Label](/knowledge/cip-classification-label.md)
* [Multi-Channel Communication Protocol](/knowledge/multi-channel-communication-protocol.md)
