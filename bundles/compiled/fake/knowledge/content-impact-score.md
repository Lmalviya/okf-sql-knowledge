---
type: Calculation
title: Content Impact Score (CIS)
description: Measures potential impact of manipulated content.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 37
---

# Definition

CIS = CMS \times MPS \times \frac{\text{netinflscore}}{100}

# Columns used

* [moderationaction](/tables/moderationaction.md): `netinflscore`

# Depends on

* [Content Manipulation Score (CMS)](/knowledge/content-manipulation-score.md)
* [Moderation Priority Score (MPS)](/knowledge/moderation-priority-score.md)

# Used by

* [Trusted Content Creator](/knowledge/trusted-content-creator.md)
* [Mass Manipulation Campaign](/knowledge/mass-manipulation-campaign.md)
* [Content Distribution Pattern Score (CDPS)](/knowledge/content-distribution-pattern-score.md)
* [Content Amplification Effect (CAE)](/knowledge/content-amplification-effect.md)
