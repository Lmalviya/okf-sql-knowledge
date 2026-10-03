---
type: Business Rule
title: Reputational Risk
description: Measures the potential risk to an account’s reputation based on past moderation actions and low reputation scores.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 72
---

# Definition

An account with reputscore < 30 and high abuserepnum, prioritized by the top quartile of abuse reports.

# Columns used

* [moderationaction](/tables/moderationaction.md): `abuserepnum`, `reputscore`
