---
type: Calculation
title: Order Modification Intensity (OMI)
description: Measures how frequently a trader modifies orders relative to their cancellation rate.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 1
---

# Definition

OMI = \frac{\text{modfreq}}{1 - \text{cancelpct}} \text{ (undefined if cancelpct = 1)}

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `cancelpct`, `modfreq`

# Used by

* [Market Manipulation Pattern: Layering/Spoofing](/knowledge/market-manipulation-pattern-layering-spoofing.md)
* [High Cancellation/Modification Trader](/knowledge/high-cancellation-modification-trader.md)
* [Aggressive Trading Intensity (ATI)](/knowledge/aggressive-trading-intensity.md)
* [Cross-Modification Ratio (CMR)](/knowledge/cross-modification-ratio.md)
