---
type: Calculation
title: Capital-Adjusted Investigation Intensity (CAII)
description: Normalizes the investigation intensity index by the trader's account balance, showing investigation focus relative to trader size.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 55
---

# Definition

CAII = \frac{\text{III}}{\text{Max}(1000, \text{acctbal})} \\ \text{where III is Investigation Intensity Index .}

# Columns used

* [trader](/tables/trader.md): `acctbal`

# Depends on

* [Investigation Intensity Index (III)](/knowledge/investigation-intensity-index.md)
