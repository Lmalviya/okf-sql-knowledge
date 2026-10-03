---
type: Calculation
title: Credit Quality Index (CQI)
description: Comprehensive measure of overall credit quality incorporating credit score and utilization.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 31
---

# Definition

CQI = 0.6 × \frac{credscore}{850} + 0.4 × (1 - CUR), \text{where CUR is the Credit Utilization Ratio}

# Columns used

* [credit_and_compliance](/tables/credit_and_compliance.md): `credscore`

# Depends on

* [Credit Utilization Ratio (CUR)](/knowledge/credit-utilization-ratio.md)

# Used by

* [Premium Banking Candidate](/knowledge/premium-banking-candidate.md)
* [Credit Building Opportunity](/knowledge/credit-building-opportunity.md)
* [Cross-Sell Priority](/knowledge/cross-sell-priority.md)
