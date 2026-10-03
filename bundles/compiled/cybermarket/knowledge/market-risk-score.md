---
type: Calculation
title: Market Risk Score (MRS)
description: Calculates overall risk level of a market based on multiple factors
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 10
---

# Definition

MRS = \frac{dlyflow}{1000} + (esccomprate \times 0.2) + (interscore \times 0.3) + (vendcount \times 0.1) - \frac{mktspan}{100}, \text{where higher scores indicate greater risk exposure requiring enhanced monitoring.}

# Columns used

* [markets](/tables/markets.md): `mktspan`, `dlyflow`, `vendcount`, `interscore`, `esccomprate`

# Used by

* [High-Risk Market](/knowledge/high-risk-market.md)
