---
type: Value Illustration
title: Credit Utilization Impact
description: Illustrates how credit utilization affects credit scores.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 23
---

# Definition

Credit Utilization (credutil) ranges from 0-1 (or above). Utilization under 0.30 is optimal for credit scores, 0.30-0.50 has moderate negative impact, 0.50-0.70 has significant negative impact, and above 0.70 severely impacts credit scores.

# Columns used

* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `credutil`

# Depends on

* [Credit Utilization Ratio (CUR)](/knowledge/credit-utilization-ratio.md)
