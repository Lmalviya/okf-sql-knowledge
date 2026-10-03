---
type: Business Rule
title: Technical Breakout
description: Identifies when price breaks significant technical levels with volume.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 19
---

# Definition

Market condition where price exceeds the highspotday or falls below lowspotday with volume (volday) at least 50% above the 30-day average.

# Columns used

* [marketstats](/tables/marketstats.md): `volday`, `highspotday`, `lowspotday`
