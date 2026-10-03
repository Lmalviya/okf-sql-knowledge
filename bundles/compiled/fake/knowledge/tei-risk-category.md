---
type: Business Rule
title: TEI Risk Category
description: A categorical risk level assigned based on an account's TEI Quartile.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 79
---

# Definition

A category assigned as 'Low Risk' (Quartile 1), 'Moderate Risk' (Quartile 2), 'High Risk' (Quartile 3), or 'Very High Risk' (Quartile 4) based on the account's calculated TEI Quartile.

# Depends on

* [TEI quartile](/knowledge/tei-quartile.md)
