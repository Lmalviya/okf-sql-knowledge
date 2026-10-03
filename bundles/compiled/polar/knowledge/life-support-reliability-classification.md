---
type: Business Rule
title: Life Support Reliability Classification (LSRC)
description: Categorizes life support systems into reliability classes based on their LSSR score for operational decision-making.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 51
---

# Definition

Life support systems are classified into three reliability categories: 'High Reliability' WHEN (LSSR >= 0.8), 'Moderate Reliability' WHEN (LSSR >= 0.6 AND LSSR < 0.8), and 'Low Reliability' WHEN (LSSR < 0.6).

# Depends on

* [Life Support System Reliability (LSSR)](/knowledge/life-support-system-reliability.md)
