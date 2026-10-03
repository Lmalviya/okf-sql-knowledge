---
type: Value Illustration
title: detection_score_profile.behavior_scores.botlikscore
description: Illustrates bot likelihood scoring.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 29
---

# Definition

Ranges from 0 to 100. Scores above 70 strongly indicate bot behavior, while scores below 20 suggest human-like behavior patterns.

# Columns used

* [securitydetection](/tables/securitydetection.md): `detection_score_profile`

# Used by

* [Latest Bot Likelihood Score (LBS)](/knowledge/latest-bot-likelihood-score.md)
