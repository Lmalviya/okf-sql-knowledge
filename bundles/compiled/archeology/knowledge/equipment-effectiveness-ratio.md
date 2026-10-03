---
type: Calculation
title: Equipment Effectiveness Ratio (EER)
description: Evaluates how effectively equipment was utilized based on power consumption and scan quality relative to equipment capability.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 39
---

# Definition

EER = \frac{SQS \times EquipStatus\_value}{PowerLevel \times (101 - EquipAge\_days) / 365} \times 25, \text{ where SQS is the Scan Quality Score, EquipStatus_value is 1.0 for 'Excellent' to 0.2 for 'Poor', and EquipAge_days is days since EquipTune, with higher values indicating more efficient use of equipment relative to condition.}

# Columns used

* [equipment](/tables/equipment.md): `equiptune`, `equipstatus`, `powerlevel`

# Depends on

* [Scan Quality Score (SQS)](/knowledge/scan-quality-score.md)

# Used by

* [Equipment Optimization Opportunity](/knowledge/equipment-optimization-opportunity.md)
