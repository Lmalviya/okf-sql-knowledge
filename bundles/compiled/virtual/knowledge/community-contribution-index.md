---
type: Calculation
title: Community Contribution Index (CCI)
description: Measures a fan's overall contribution to the virtual idol community
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 17
---

# Definition

CCI = (CCIS \times 0.4) + (SIM \times 0.3) + (collabcount \times 0.1) + (FEI \times 0.2), \text{ balancing content creation, social influence, collaboration activity, and general engagement.}

# Columns used

* [socialcommunity](/tables/socialcommunity.md): `collabcount`

# Depends on

* [Fan Engagement Index (FEI)](/knowledge/fan-engagement-index.md)
* [Content Creation Impact Score (CCIS)](/knowledge/content-creation-impact-score.md)
* [Social Influence Multiplier (SIM)](/knowledge/social-influence-multiplier.md)

# Used by

* [Community Pillar](/knowledge/community-pillar.md)
