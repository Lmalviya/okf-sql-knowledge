---
type: Calculation
title: Cross-Platform Risk Index (CPRI)
description: Evaluates risk across multiple platform types for the same account.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 30
---

# Definition

CPRI = SRS \times (1 + 0.2 \times \text{ipcountrynum})

# Columns used

* [technicalinfo](/tables/technicalinfo.md): `ipcountrynum`

# Depends on

* [Security Risk Score (SRS)](/knowledge/security-risk-score.md)

# Used by

* [Cross-Platform Threat](/knowledge/cross-platform-threat.md)
* [Cross-Platform Correlation Score (CPCS)](/knowledge/cross-platform-correlation-score.md)
