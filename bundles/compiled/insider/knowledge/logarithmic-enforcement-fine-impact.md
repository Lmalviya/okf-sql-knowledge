---
type: Calculation
title: Logarithmic Enforcement Fine Impact (LEFI)
description: Calculates the log-scaled financial impact ratio of enforcement fines, emphasizing order of magnitude.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 35
---

# Definition

LEFI = \text{EFIR} \times \log_{10}(\text{Max}(10, \text{penamt})) \\ \text{where EFIR is the Enforcement Financial Impact Ratio .}

# Columns used

* [enforcementactions](/tables/enforcementactions.md): `penamt`

# Depends on

* [Enforcement Financial Impact Ratio (EFIR)](/knowledge/enforcement-financial-impact-ratio.md)

# Used by

* [Elevated Regulatory Scrutiny](/knowledge/elevated-regulatory-scrutiny.md)
* [Weighted Investigation Score (WIS)](/knowledge/weighted-investigation-score.md)
