---
type: Business Rule
title: Account Inactivity
description: A condition indicating that an account has not demonstrated recent activity based on available data proxies.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 86
---

# Definition

Condition met when: \text{last activity proxy time} < (\text{CURRENT_DATE} - \text{'90 days'})

# Depends on

* [last activity proxy time](/knowledge/last-activity-proxy-time.md)
