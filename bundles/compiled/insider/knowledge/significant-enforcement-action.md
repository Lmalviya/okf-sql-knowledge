---
type: Business Rule
title: Significant Enforcement Action
description: Categorizes enforcement actions that represent substantial penalties or restrictions.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 19
---

# Definition

An action is considered a Significant Enforcement Action if `penimp` is 'Fine' or 'Ban' OR `acttake` is 'Suspension' OR `busrestr` is 'Full'.

# Columns used

* [enforcementactions](/tables/enforcementactions.md): `acttake`, `penimp`, `busrestr`

# Depends on

* [Boosted Insider Leakage Score (BILS)](/knowledge/boosted-insider-leakage-score.md)
* [Market-Adjusted Pattern Anomaly (MAPA)](/knowledge/market-adjusted-pattern-anomaly.md)

# Used by

* [Financially Impactful Enforcement Case](/knowledge/financially-impactful-enforcement-case.md)
* [Escalated Compliance Failure](/knowledge/escalated-compliance-failure.md)
