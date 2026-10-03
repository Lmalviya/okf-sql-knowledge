---
type: Value Illustration
title: detection_score_profile.overall.confval
description: Illustrates confidence value in detection scores.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 20
---

# Definition

Ranges from 0 to 1. Values above 0.8 indicate high-confidence detections, while values below 0.3 suggest uncertain results requiring manual review.

# Columns used

* [securitydetection](/tables/securitydetection.md): `detection_score_profile`
