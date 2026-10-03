---
type: Calculation
title: Pattern Anomaly Score (PAS)
description: Measures the deviation of a trader's pattern similarity from their peer correlation, potentially indicating unique illicit behavior.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 4
---

# Definition

PAS = |\text{patsim} - \text{peercorr}|

# Columns used

* [advancedbehavior](/tables/advancedbehavior.md): `patsim`, `peercorr`

# Used by

* [Combined Manipulation Indicator (CMI)](/knowledge/combined-manipulation-indicator.md)
* [Market-Adjusted Pattern Anomaly (MAPA)](/knowledge/market-adjusted-pattern-anomaly.md)
* [Peer Mimicry Suspicion](/knowledge/peer-mimicry-suspicion.md)
* [Unique Pattern Deviation Ratio (UPDR)](/knowledge/unique-pattern-deviation-ratio.md)
