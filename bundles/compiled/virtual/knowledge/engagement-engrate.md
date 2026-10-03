---
type: Value Illustration
title: engagement.engrate
description: Explains the calculation basis and business significance of fan engagement rate
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 5
---

# Definition

Engagement rate (engrate) typically ranges from 0 to 1.000, with higher values indicating more active fans. 0-0.200 represents low engagement (viewing only without participation), 0.201-0.500 indicates moderate engagement (occasional comments and likes), 0.501-0.800 shows high engagement (frequent comments and sharing), and 0.801-1.000 represents ultra-high engagement (comprehensive deep participation in content co-creation). Platforms generally consider rates above 0.500 as quality fans.

# Columns used

* [engagement](/tables/engagement.md): `engrate`

# Used by

* [Churn Candidate](/knowledge/churn-candidate.md)
* [Silent Supporter](/knowledge/silent-supporter.md)
* [Multi-Idol Supporter](/knowledge/multi-idol-supporter.md)
* [Content Quality to Engagement Ratio (CQER)](/knowledge/content-quality-to-engagement-ratio.md)
* [Tier-Stuck Veteran](/knowledge/tier-stuck-veteran.md)
