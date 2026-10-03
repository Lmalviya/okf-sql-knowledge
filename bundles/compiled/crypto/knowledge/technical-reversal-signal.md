---
type: Business Rule
title: Technical Reversal Signal
description: Identifies strong indications of potential market direction reversal.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 42
---

# Definition

A market condition where Technical Signal Strength exceeds 8 in absolute value while simultaneously showing Momentum Divergence, providing reinforcing signals of a potential trend reversal.

# Depends on

* [Momentum Divergence](/knowledge/momentum-divergence.md)
* [Technical Signal Strength](/knowledge/technical-signal-strength.md)
