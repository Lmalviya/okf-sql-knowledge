---
type: Value Illustration
title: Credit Score Categories
description: Illustrates the meaning of different credit score ranges.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 20
---

# Definition

Credit scores (credscore) typically range from 300-850. 300-579: Poor, 580-669: Fair, 670-739: Good, 740-799: Very Good, 800-850: Excellent, Otherwise: Unknown. Higher scores indicate lower credit risk.

# Columns used

* [credit_and_compliance](/tables/credit_and_compliance.md): `credscore`
