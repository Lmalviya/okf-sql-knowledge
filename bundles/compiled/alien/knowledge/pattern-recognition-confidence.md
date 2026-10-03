---
type: Calculation
title: Pattern Recognition Confidence (PRC)
description: Measures confidence in identified signal patterns based on multiple factors.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 38
---

# Definition

$\text{PRC} = (\text{RepeatCount} > 1 ? 1 + \log_{10}(\text{RepeatCount}) : 0.5) \times (\text{EntropyVal} < 0.9 ? 1 : 0.3) \times \text{SCR}$, where SCR (Signal Complexity Ratio) provides complexity weighting.

# Columns used

* [signalclassification](/tables/signalclassification.md): `repeatcount`, `entropyval`

# Depends on

* [Signal Complexity Ratio (SCR)](/knowledge/signal-complexity-ratio.md)

# Used by

* [Research Critical Signal](/knowledge/research-critical-signal.md)
