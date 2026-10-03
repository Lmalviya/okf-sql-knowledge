---
type: Calculation
title: Latest Bot Likelihood Score (LBS)
description: The most recent bot likelihood score for an account based on security detection timestamps.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 71
---

# Definition

LBS_a = \text{botlikscore}(\max_{t \in T_a} \text{detecttime}_t) where T_a is the set of all detection timestamps for account a

# Columns used

* [securitydetection](/tables/securitydetection.md): `detecttime`

# Depends on

* [detection_score_profile.behavior_scores.botlikscore](/knowledge/detection-score-profile-behavior-scores-botlikscore.md)
