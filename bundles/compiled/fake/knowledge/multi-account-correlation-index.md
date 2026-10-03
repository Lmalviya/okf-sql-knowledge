---
type: Calculation
title: Multi-Account Correlation Index (MACI)
description: Measures behavioral correlation across linked accounts.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 52
---

# Definition

MACI = \frac{\sum_{i=1}^{n} \sum_{j=i+1}^{n} \text{corr}(i,j)}{\binom{n}{2}} where n is linked accounts

# Depends on

* [Automated Behavior Score (ABS)](/knowledge/automated-behavior-score.md)
* [Network Manipulation Index (NMI)](/knowledge/network-manipulation-index.md)

# Used by

* [Network Synchronization Index (NSI)](/knowledge/network-synchronization-index.md)
* [Cross-Platform Correlation Score (CPCS)](/knowledge/cross-platform-correlation-score.md)
* [Cross-Platform Bot Network](/knowledge/cross-platform-bot-network.md)
