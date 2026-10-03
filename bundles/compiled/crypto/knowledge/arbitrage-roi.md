---
type: Calculation
title: Arbitrage ROI
description: Calculates the potential return on investment for an arbitrage opportunity.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 35
---

# Definition

Arbitrage ROI = \frac{AOS \times dealquote}{feetotal \times 2}, \text{where } AOS \text{ is the Arbitrage Opportunity Score and } feetotal \text{ is multiplied by 2 to account for fees on both transactions involved in arbitrage.}

# Columns used

* [orders](/tables/orders.md): `dealquote`
* [fees](/tables/fees.md): `feetotal`

# Depends on

* [Arbitrage Opportunity Score (AOS)](/knowledge/arbitrage-opportunity-score.md)
* [True Cost of Execution](/knowledge/true-cost-of-execution.md)

# Used by

* [High-Quality Arbitrage Opportunity](/knowledge/high-quality-arbitrage-opportunity.md)
