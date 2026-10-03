---
type: Calculation
title: Content Distribution Pattern Score (CDPS)
description: Analyzes patterns in content posting and sharing.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 54
---

# Definition

CDPS = 0.4 \times \text{entropy}(\text{posttimes}) + 0.3 \times \text{burstiness} + 0.3 \times (1 - \text{periodicity})

# Depends on

* [Content Manipulation Score (CMS)](/knowledge/content-manipulation-score.md)
* [Content Impact Score (CIS)](/knowledge/content-impact-score.md)

# Used by

* [Reputation Manipulation Ring](/knowledge/reputation-manipulation-ring.md)
