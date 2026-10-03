---
type: Calculation
title: Customer Engagement Score (CES)
description: Quantifies how actively a customer uses bank products and services.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:54+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 7
---

# Definition

CES = 0.4 × produsescore + 0.3 × chanusescore + 0.2 × bankrelscore + 0.1 × \frac{custservint}{10}, \text{where each component is capped at 1.0}

# Columns used

* [bank_and_transactions](/tables/bank_and_transactions.md): `bankrelscore`
* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `custservint`, `produsescore`, `chanusescore`

# Used by

* [Customer Retention Risk (CRR)](/knowledge/customer-retention-risk.md)
* [Banking Relationship Strength (BRS)](/knowledge/banking-relationship-strength.md)
* [Cross-Sell Priority](/knowledge/cross-sell-priority.md)
* [High Engagement Criteria](/knowledge/high-engagement-criteria.md)
