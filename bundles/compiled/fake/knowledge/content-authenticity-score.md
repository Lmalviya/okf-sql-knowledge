---
type: Calculation
title: Content Authenticity Score (CAS)
description: Aggregates multiple authenticity indicators into a single score.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 1
---

# Definition

CAS = 0.3 \times \text{authenscore} + 0.3 \times \text{cntuniqscore} + 0.4 \times \text{convnatval} where values are normalized to [0,1]

# Columns used

* [moderationaction](/tables/moderationaction.md): `authenscore`
* [contentbehavior](/tables/contentbehavior.md): `cntuniqscore`
* [messaginganalysis](/tables/messaginganalysis.md): `convnatval`

# Used by

* [Enhanced Trust Score (ETS)](/knowledge/enhanced-trust-score.md)
* [Content Security Index (CSI)](/knowledge/content-security-index.md)
* [Automated Behavior Score (ABS)](/knowledge/automated-behavior-score.md)
