---
type: Calculation
title: Content Quality Consistency (CQC)
description: Measures the consistency of a fan's content quality relative to their engagement consistency
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 36
---

# Definition

CQC = contqualrate \times intconsist \times \frac{ugcval}{10}, \text{ where intconsist measures interaction consistency on a scale of 0-1.}

# Columns used

* [preferencesandsettings](/tables/preferencesandsettings.md): `intconsist`

# Depends on

* [socialcommunity.community_engagement.content_creation.contqualrate](/knowledge/socialcommunity-community-engagement-content-creation-contqualrate.md)

# Used by

* [Quality Inconsistent Creator](/knowledge/quality-inconsistent-creator.md)
