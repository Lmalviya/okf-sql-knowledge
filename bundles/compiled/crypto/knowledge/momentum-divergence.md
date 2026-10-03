---
type: Business Rule
title: Momentum Divergence
description: Identifies when price action diverges from momentum indicators.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 17
---

# Definition

Market condition where price makes new highs/lows while momentum indicators (buyforce, sellforce) move in the opposite direction.

# Used by

* [Technical Signal Strength](/knowledge/technical-signal-strength.md)
* [Technical Reversal Signal](/knowledge/technical-reversal-signal.md)
* [Perfect Technical Setup](/knowledge/perfect-technical-setup.md)
