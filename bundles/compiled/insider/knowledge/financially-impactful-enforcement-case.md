---
type: Business Rule
title: Financially Impactful Enforcement Case
description: Identifies traders who faced significant enforcement actions with a high financial impact relative to their account size.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 48
---

# Definition

A trader subject to a Significant Enforcement Action  AND whose Enforcement Financial Impact Ratio (EFIR)  is greater than 0.1.

# Depends on

* [Enforcement Financial Impact Ratio (EFIR)](/knowledge/enforcement-financial-impact-ratio.md)
* [Significant Enforcement Action](/knowledge/significant-enforcement-action.md)

# Used by

* [Costly High-Frequency Risk Enforcement](/knowledge/costly-high-frequency-risk-enforcement.md)
