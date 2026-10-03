---
type: Business Rule
title: Over-Leveraged Position
description: Identifies positions with excessive leverage relative to market volatility.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 13
---

# Definition

A position where the leverage (posmagn) multiplied by the volatility measure (volmeter) exceeds 500, indicating high risk exposure.

# Columns used

* [marketstats](/tables/marketstats.md): `volmeter`

# Used by

* [Critically Over-Leveraged Position](/knowledge/critically-over-leveraged-position.md)
* [Flash Crash Vulnerability](/knowledge/flash-crash-vulnerability.md)
