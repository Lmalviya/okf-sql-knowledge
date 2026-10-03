---
type: Calculation
title: Incident Impact Factor (IIF)
description: Measures the potential impact of incidents based on risk exposure and resolution efficiency.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 55
---

# Definition

IIF = \text{RES} \times (1 - \text{IRE})

# Depends on

* [Risk Exposure Score (RES)](/knowledge/risk-exposure-score.md)
* [Incident Resolution Efficiency (IRE)](/knowledge/incident-resolution-efficiency.md)

# Used by

* [Incident-Prone Compliance Flow](/knowledge/incident-prone-compliance-flow.md)
