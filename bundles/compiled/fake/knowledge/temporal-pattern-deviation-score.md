---
type: Calculation
title: Temporal Pattern Deviation Score (TPDS)
description: Measures deviation from established temporal activity patterns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 50
---

# Definition

TPDS = \sqrt{\sum_{i=1}^{24} (\frac{\text{obsfreq}_i - \text{expfreq}_i}{\text{expfreq}_i})^2}

# Depends on

* [Account Activity Frequency (AAF)](/knowledge/account-activity-frequency.md)
* [Behavioral Anomaly Score (BAS)](/knowledge/behavioral-anomaly-score.md)

# Used by

* [Behavioral Consistency Score (BCS)](/knowledge/behavioral-consistency-score.md)
* [Behavioral Pattern Anomaly](/knowledge/behavioral-pattern-anomaly.md)
* [Persistent Pattern Anomaly](/knowledge/persistent-pattern-anomaly.md)
