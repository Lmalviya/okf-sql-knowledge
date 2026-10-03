---
type: Calculation
title: Transport Safety Rating (TSR)
description: Safety rating for transport considering multiple factors.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 35
---

# Definition

TSR = \frac{\text{RCP}}{100} \times (1 - \text{TRS}) \times \text{HQI}

# Depends on

* [Route Completion Percentage (RCP)](/knowledge/route-completion-percentage.md)
* [Total Risk Score (TRS)](/knowledge/total-risk-score.md)
* [Handling Quality Index (HQI)](/knowledge/handling-quality-index.md)

# Used by

* [Critical Transport Condition](/knowledge/critical-transport-condition.md)
* [Critical Route Status](/knowledge/critical-route-status.md)
* [Transport Safety Alert](/knowledge/transport-safety-alert.md)
* [Critical Safety Condition](/knowledge/critical-safety-condition.md)
