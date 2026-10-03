---
type: Business Rule
title: Financial Stress Indicator
description: Identifies customers showing multiple signs of financial difficulty.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 42
---

# Definition

A customer with FVS (Financial Vulnerability Score) > 0.7, recent payment issues (delinqcount > 0 or latepaycount > 0 in past six months), and negative Net Worth.

# Columns used

* [credit_and_compliance](/tables/credit_and_compliance.md): `delinqcount`, `latepaycount`

# Depends on

* [Net Worth](/knowledge/net-worth.md)
* [Financial Vulnerability Score (FVS)](/knowledge/financial-vulnerability-score.md)
