---
type: Business Rule
title: High Velocity Suspicion Trader
description: Identifies traders exhibiting both high risk-adjusted turnover and a high suspicious activity index.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 66
---

# Definition

A trader with a high Risk-Adjusted Turnover (RAT)  (e.g., > 1.0) AND a high Suspicious Activity Index (SAI)  (e.g., > 0.6).

# Depends on

* [Suspicious Activity Index (SAI)](/knowledge/suspicious-activity-index.md)
* [Risk-Adjusted Turnover (RAT)](/knowledge/risk-adjusted-turnover.md)
