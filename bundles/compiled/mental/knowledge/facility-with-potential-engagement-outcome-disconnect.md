---
type: Business Rule
title: Facility with Potential Engagement-Outcome Disconnect
description: Identifies facilities where high therapy engagement scores do not seem to translate into expected functional improvements or recovery progression.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 58
---

# Definition

A facility where TES > 2.0 AND RTI < 0.8, \text{indicating high Therapy Engagement Score (TES) but a low Recovery Trajectory Index (RTI).}

# Depends on

* [Therapy Engagement Score (TES)](/knowledge/therapy-engagement-score.md)
* [Recovery Trajectory Index (RTI)](/knowledge/recovery-trajectory-index.md)
