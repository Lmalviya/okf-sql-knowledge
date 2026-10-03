---
type: Calculation
title: Customer Retention Risk (CRR)
description: Calculates risk of customer attrition based on engagement and satisfaction metrics.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 34
---

# Definition

CRR = 0.4 × churnrate + 0.3 × (1 - CES) + 0.3 × \frac{complainthist}{3}, \text{where CES is the Customer Engagement Score and complainthist is converted to numeric (Low=1, Medium=2, High=3)}

# Columns used

* [core_record](/tables/core_record.md): `churnrate`
* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `complainthist`

# Depends on

* [Customer Engagement Score (CES)](/knowledge/customer-engagement-score.md)

# Used by

* [Relationship Attrition Risk](/knowledge/relationship-attrition-risk.md)
