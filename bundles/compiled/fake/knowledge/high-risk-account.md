---
type: Business Rule
title: High-Risk Account
description: Identifies accounts requiring immediate attention.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 10
---

# Definition

An account with SRS > 0.8 and at least one active security detection with threatlvl = 'Critical'

# Depends on

* [Security Risk Score (SRS)](/knowledge/security-risk-score.md)

# Used by

* [Cross-Platform Threat](/knowledge/cross-platform-threat.md)
