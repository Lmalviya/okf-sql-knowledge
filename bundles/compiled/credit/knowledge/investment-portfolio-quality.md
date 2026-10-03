---
type: Calculation
title: Investment Portfolio Quality (IPQ)
description: Evaluates the quality and performance of customer's investment allocations.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 37
---

# Definition

IPQ = 0.4 × RAR + 0.4 × \frac{investamt}{totassets} + 0.2 × \frac{chaninvdatablock.invcluster.investexp}{3}, \text{where RAR is the Risk-Adjusted Return and investexp is converted to numeric (Limited=1, Moderate=2, Extensive=3)}

# Columns used

* [expenses_and_assets](/tables/expenses_and_assets.md): `investamt`, `totassets`
* [bank_and_transactions](/tables/bank_and_transactions.md): `chaninvdatablock`

# Depends on

* [Risk-Adjusted Return (RAR)](/knowledge/risk-adjusted-return.md)
