---
type: Calculation
title: Scientific Equipment Reliability (SER)
description: Quantifies the reliability of scientific equipment based on calibration status and measurement accuracy.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 8
---

# Definition

SER = measurementaccuracypercent \times \begin{cases} 1.0 & \text{if calibrationstatus = 'Valid'} \\ 0.7 & \text{if calibrationstatus = 'Due'} \\ 0.3 & \text{if calibrationstatus = 'Expired'} \end{cases}, \text{ where valid calibration and high accuracy result in more reliable scientific data.}

# Columns used

* [scientific](/tables/scientific.md): `calibrationstatus`, `measurementaccuracypercent`

# Used by

* [Scientific Data Reliability Classification](/knowledge/scientific-data-reliability-classification.md)
* [Scientific Mission Success Probability (SMSP)](/knowledge/scientific-mission-success-probability.md)
* [Critical Scientific Equipment Status (CSES)](/knowledge/critical-scientific-equipment-status.md)
