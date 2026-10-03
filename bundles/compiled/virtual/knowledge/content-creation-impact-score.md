---
type: Calculation
title: Content Creation Impact Score (CCIS)
description: Measures the impact of fan-created content on the community
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 12
---

# Definition

CCIS = contqualrate \times \left(\frac{ugcval}{10}\right) \times \left(1 + \frac{follcount}{100} \times 0.5\right), \text{ where content quality is multiplied by normalized content volume and amplified by follower reach.}

# Used by

* [Community Contribution Index (CCI)](/knowledge/community-contribution-index.md)
