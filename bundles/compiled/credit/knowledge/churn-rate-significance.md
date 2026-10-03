---
type: Value Illustration
title: Churn Rate Significance
description: Illustrates what different churn rate values indicate about customer retention risk.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 29
---

# Definition

Churn rate (churnrate) ranges from 0-1. Values below 0.1 indicate low attrition risk, 0.1-0.2 indicates moderate risk, 0.2-0.3 indicates high risk, and above 0.3 indicates severe risk of customer loss requiring immediate relationship management intervention.

# Columns used

* [core_record](/tables/core_record.md): `churnrate`
