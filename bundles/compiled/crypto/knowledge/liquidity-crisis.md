---
type: Business Rule
title: Liquidity Crisis
description: Identifies periods of severely reduced market liquidity.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 16
---

# Definition

Market conditions where the Liquidity Ratio falls below 0.01, indicating insufficient market depth relative to typical trading volume.

# Depends on

* [Liquidity Ratio](/knowledge/liquidity-ratio.md)

# Used by

* [Flash Crash Vulnerability](/knowledge/flash-crash-vulnerability.md)
