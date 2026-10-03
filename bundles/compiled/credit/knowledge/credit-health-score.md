---
type: Calculation
title: Credit Health Score (CHS)
description: Composite score measuring overall credit wellness based on multiple factors.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:54+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 5
---

# Definition

CHS = 0.4 × \frac{credscore}{850} + 0.2 × (1 - credutil) + 0.2 × (1 - debincratio) + 0.1 × \frac{credageyrs}{20} + 0.1 × (1 - \frac{delinqcount + latepaycount + choffs + bankr}{10}), \text{where each component is capped at 1.0}

# Columns used

* [employment_and_income](/tables/employment_and_income.md): `debincratio`
* [credit_and_compliance](/tables/credit_and_compliance.md): `credscore`, `delinqcount`, `latepaycount`, `choffs`, `bankr`, `credageyrs`
* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `credutil`

# Used by

* [Credit Health Momentum (CHM)](/knowledge/credit-health-momentum.md)
