---
type: Business Rule
title: High-Risk Market
description: Identifies markets with significant operational risk factors
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 20
---

# Definition

A market with MRS > 500, having more than 100 vendors, a daily flow exceeding 5000 transactions, and at least one 'High' security alert. These markets typically have the highest potential for illicit activity and represent priority monitoring targets for investigators.

# Depends on

* [Market Risk Score (MRS)](/knowledge/market-risk-score.md)

# Used by

* [Priority Investigation Target](/knowledge/priority-investigation-target.md)
