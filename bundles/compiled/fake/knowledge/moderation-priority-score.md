---
type: Calculation
title: Moderation Priority Score (MPS)
description: Calculates priority for moderation review.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 9
---

# Definition

MPS = 0.3 \times \frac{\text{abuserepnum}}{1000} + 0.4 \times \text{impactval} + 0.3 \times \text{riskval}

# Columns used

* [moderationaction](/tables/moderationaction.md): `abuserepnum`, `impactval`

# Used by

* [Content Impact Score (CIS)](/knowledge/content-impact-score.md)
