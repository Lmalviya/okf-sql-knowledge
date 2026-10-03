---
type: Calculation
title: Banking Relationship Strength (BRS)
description: Quantifies the depth and quality of a customer's banking relationship.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 38
---

# Definition

BRS = 0.3 × bankrelscore + 0.3 × (1 - churnrate) + 0.4 × CES, \text{where CES is the Customer Engagement Score}

# Columns used

* [core_record](/tables/core_record.md): `churnrate`
* [bank_and_transactions](/tables/bank_and_transactions.md): `bankrelscore`

# Depends on

* [Customer Engagement Score (CES)](/knowledge/customer-engagement-score.md)

# Used by

* [Digital Channel Opportunity](/knowledge/digital-channel-opportunity.md)
