---
type: Calculation
title: Life Support System Reliability (LSSR)
description: Evaluates the reliability of life support systems under polar conditions
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 33
---

# Definition

LSSR = 0.7 × ORS + 0.3 × TIE

# Depends on

* [Operational Readiness Score (ORS)](/knowledge/operational-readiness-score.md)
* [Thermal Insulation Efficiency (TIE)](/knowledge/thermal-insulation-efficiency.md)

# Used by

* [Emergency Response Readiness Status (ERRS)](/knowledge/emergency-response-readiness-status.md)
* [Life Support Reliability Classification (LSRC)](/knowledge/life-support-reliability-classification.md)
