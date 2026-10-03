---
type: Calculation
title: Combined Maintenance Risk (CMR)
description: Evaluates overall maintenance risk considering compliance and incidents.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 32
---

# Definition

CMR = (1 - \text{MCS}) \times (1 + \frac{\text{TBS}}{5}) \times (1 - \text{LHI})

# Depends on

* [Maintenance Compliance Score (MCS)](/knowledge/maintenance-compliance-score.md)
* [Temperature Breach Severity (TBS)](/knowledge/temperature-breach-severity.md)
* [Logger Health Index (LHI)](/knowledge/logger-health-index.md)

# Used by

* [Logger Reliability Score (LRS)](/knowledge/logger-reliability-score.md)
* [High Maintenance Priority](/knowledge/high-maintenance-priority.md)
* [Logger Critical State](/knowledge/logger-critical-state.md)
* [Urgency Rank](/knowledge/urgency-rank.md)
