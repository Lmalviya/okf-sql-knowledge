---
type: Business Rule
title: Digital Channel Opportunity
description: Identifies customers who would benefit from increased digital engagement.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 44
---

# Definition

A customer with low digital engagement (chaninvdatablock.onlineuse not 'High' and chaninvdatablock.mobileuse not 'High') but high BRS (Banking Relationship Strength > 0.7) and multiple products (produsescore > 0.5).

# Columns used

* [bank_and_transactions](/tables/bank_and_transactions.md): `chaninvdatablock`
* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `produsescore`

# Depends on

* [Banking Relationship Strength (BRS)](/knowledge/banking-relationship-strength.md)
