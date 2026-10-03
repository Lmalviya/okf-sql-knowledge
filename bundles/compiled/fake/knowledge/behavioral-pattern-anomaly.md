---
type: Business Rule
title: Behavioral Pattern Anomaly
description: Identifies accounts with inconsistent behavioral patterns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 61
---

# Definition

An account with BCS < 0.3 and TPDS > 0.7 and is not a Trusted Account

# Depends on

* [Behavioral Consistency Score (BCS)](/knowledge/behavioral-consistency-score.md)
* [Temporal Pattern Deviation Score (TPDS)](/knowledge/temporal-pattern-deviation-score.md)
* [Trusted Account](/knowledge/trusted-account.md)

# Used by

* [Persistent Pattern Anomaly](/knowledge/persistent-pattern-anomaly.md)
