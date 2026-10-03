---
type: Calculation
title: Cross-Platform Correlation Score (CPCS)
description: Measures behavioral correlation across platforms.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 59
---

# Definition

CPCS = CPRI \times MACI \times (1 + \frac{\text{platformlinks}}{10})

# Depends on

* [Cross-Platform Risk Index (CPRI)](/knowledge/cross-platform-risk-index.md)
* [Multi-Account Correlation Index (MACI)](/knowledge/multi-account-correlation-index.md)

# Used by

* [Cross-Platform Bot Network](/knowledge/cross-platform-bot-network.md)
* [Multi-Platform Threat Network](/knowledge/multi-platform-threat-network.md)
