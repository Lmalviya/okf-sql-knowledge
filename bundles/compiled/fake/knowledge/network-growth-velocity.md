---
type: Calculation
title: Network Growth Velocity (NGV)
description: Measures the rate of network growth considering both followers and following.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 2
---

# Definition

NGV = \sqrt{\text{followgrowrate}^2 + \text{followinggrowrate}^2}

# Used by

* [Network Trust Score (NTS)](/knowledge/network-trust-score.md)
* [Behavioral Anomaly Score (BAS)](/knowledge/behavioral-anomaly-score.md)
