---
type: Calculation
title: Content Manipulation Score (CMS)
description: Evaluates content manipulation patterns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 8
---

# Definition

CMS = 0.4 \times (1 - \text{cntuniqscore}) + 0.3 \times \text{mediareratio} + 0.3 \times (1 - \text{txtuniq})

# Columns used

* [contentbehavior](/tables/contentbehavior.md): `cntuniqscore`, `mediareratio`
* [messaginganalysis](/tables/messaginganalysis.md): `txtuniq`

# Used by

* [Content Farm](/knowledge/content-farm.md)
* [Content Security Index (CSI)](/knowledge/content-security-index.md)
* [Content Impact Score (CIS)](/knowledge/content-impact-score.md)
* [Content Manipulation Ring](/knowledge/content-manipulation-ring.md)
* [Content Distribution Pattern Score (CDPS)](/knowledge/content-distribution-pattern-score.md)
