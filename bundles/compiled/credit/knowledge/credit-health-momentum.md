---
type: Calculation
title: Credit Health Momentum (CHM)
description: Measures the trajectory of a customer's credit health over time.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 39
---

# Definition

CHM = CHS × (1 + \Delta_\text{recentbeh}), \text{where CHS is the Credit Health Score and } \Delta_\text{recentbeh} \text{ is +0.1 for 'Improving', 0 for 'Stable', and -0.1 for 'Deteriorating'}

# Columns used

* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `recentbeh`

# Depends on

* [Credit Health Score (CHS)](/knowledge/credit-health-score.md)

# Used by

* [Declining Credit Health](/knowledge/declining-credit-health.md)
