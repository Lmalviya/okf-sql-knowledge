---
type: Business Rule
title: Relationship Attrition Risk
description: Identifies customers at high risk of ending their banking relationship.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 48
---

# Definition

A customer with high CRR (Customer Retention Risk > 0.7), declining product usage (decreasing produsescore), and competitive shopping behavior (hardinq > 2 in past 3 months).

# Columns used

* [credit_and_compliance](/tables/credit_and_compliance.md): `hardinq`
* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `produsescore`

# Depends on

* [Customer Retention Risk (CRR)](/knowledge/customer-retention-risk.md)
