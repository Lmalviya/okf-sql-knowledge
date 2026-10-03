---
type: Business Rule
title: Encoded Information Transfer (EIT)
description: Characterizes signals that appear to contain deliberate information encoding.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 18
---

# Definition

Signals with $\text{ECI} > 1.8$, $\text{EntropyVal}$ between 0.3-0.7 (not random but structured), and consistent internal patterns that suggest language or data encoding schemes.

# Columns used

* [signalclassification](/tables/signalclassification.md): `entropyval`

# Depends on

* [Encoding Complexity Index (ECI)](/knowledge/encoding-complexity-index.md)
