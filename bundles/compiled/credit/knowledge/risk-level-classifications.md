---
type: Value Illustration
title: Risk Level Classifications
description: Illustrates what different risk level classifications mean.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 25
---

# Definition

Risk level (risklev) values indicate likelihood of default or financial difficulty. 'Low' indicates minimal risk, 'Medium' indicates moderate risk requiring standard monitoring, 'High' indicates significant risk requiring enhanced monitoring, and 'Very High' indicates severe risk requiring active intervention.

# Columns used

* [credit_and_compliance](/tables/credit_and_compliance.md): `risklev`
