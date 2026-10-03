---
type: Calculation
title: Resource-Demand Differential (RDD)
description: Measures the potential gap between average patient functional needs and available facility resources.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 34
---

# Definition

RDD = PFIS - FRAI, \text{comparing Patient Functional Impairment Score (PFIS) to Facility Resource Adequacy Index (FRAI)}

# Depends on

* [Patient Functional Impairment Score (PFIS)](/knowledge/patient-functional-impairment-score.md)
* [Facility Resource Adequacy Index (FRAI)](/knowledge/facility-resource-adequacy-index.md)

# Used by

* [Systemically Stressed Facility Environment](/knowledge/systemically-stressed-facility-environment.md)
