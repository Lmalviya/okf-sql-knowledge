---
type: Business Rule
title: Confirmed Evasive Layering/Spoofing
description: Identifies traders confirmed to be layering or spoofing who also exhibit high cancellation/modification behavior, suggesting deliberate evasion.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 65
---

# Definition

A trader flagged as a High Cancellation/Modification Trader  AND confirmed via Market Manipulation Pattern: Layering/Spoofing  where `risk_indicators.layerind` is 'Confirmed' or `risk_indicators.spoofprob` > 0.75.

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `risk_indicators`

# Depends on

* [Market Manipulation Pattern: Layering/Spoofing](/knowledge/market-manipulation-pattern-layering-spoofing.md)
* [High Cancellation/Modification Trader](/knowledge/high-cancellation-modification-trader.md)
