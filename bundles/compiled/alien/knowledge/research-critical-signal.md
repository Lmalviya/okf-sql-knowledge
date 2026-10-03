---
type: Business Rule
title: Research Critical Signal
description: Defines signals requiring immediate and extensive scientific resources.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 44
---

# Definition

Signals meeting Target of Opportunity (TOO) criteria with additional $\text{PRC} > 0.8$ and $\text{IMDF} < 0.5$, indicating high-quality, minimally distorted signals that show recognizable patterns warranting priority allocation of research resources.

# Depends on

* [Target of Opportunity (TOO)](/knowledge/target-of-opportunity.md)
* [Pattern Recognition Confidence (PRC)](/knowledge/pattern-recognition-confidence.md)
* [NTM Classification System](/knowledge/ntm-classification-system.md)
