---
type: Calculation
title: Correlation Between Resource Adequacy and Adherence (CRAA)
description: Measures the correlation between individual facility resource adequacy scores and treatment adherence rates.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 60
---

# Definition

CRAA = \text{CORR}(resource\_score, tar), \text{where } resource\_score \text{ is the facility's resource adequacy score, and } tar \text{ is the treatment adherence rate for the facility.}

# Depends on

* [Facility Resource Adequacy Index (FRAI)](/knowledge/facility-resource-adequacy-index.md)
* [Treatment Adherence Rate (TAR)](/knowledge/treatment-adherence-rate.md)
