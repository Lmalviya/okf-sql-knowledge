---
type: Calculation
title: Peer Correlation Z-Score
description: A normalized score indicating how many standard deviations an individual record's peer correlation ('peercorr') is away from the average peer correlation of all traders within the same trader kind ('tradekind'). Used for standardized comparison across different peer groups.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 73
---

# Definition

Z = (peercorr - AVG(peercorr) OVER (PARTITION BY tradekind)) / STDDEV_SAMP(peercorr) OVER (PARTITION BY tradekind), with Z=0 if STDDEV_SAMP is 0 or NULL.

# Columns used

* [trader](/tables/trader.md): `tradekind`
* [advancedbehavior](/tables/advancedbehavior.md): `peercorr`
