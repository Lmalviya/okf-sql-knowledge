---
type: Business Rule
title: Arbitrage Window
description: Identifies time periods with significant arbitrage opportunities across markets.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 12
---

# Definition

A market condition where the Arbitrage Opportunity Score exceeds 0.05, indicating substantial price discrepancies that can be exploited.

# Depends on

* [Arbitrage Opportunity Score (AOS)](/knowledge/arbitrage-opportunity-score.md)

# Used by

* [High-Quality Arbitrage Opportunity](/knowledge/high-quality-arbitrage-opportunity.md)
