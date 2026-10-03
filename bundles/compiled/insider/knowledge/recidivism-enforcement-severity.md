---
type: Calculation
title: Recidivism Enforcement Severity (RES)
description: Multiplies the compliance recidivism score by the enforcement financial impact, highlighting costly repeat offenders.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 53
---

# Definition

RES = \text{CRS} \times \text{EFIR} \\ \text{where CRS is Compliance Recidivism Score  and EFIR is Enforcement Financial Impact Ratio .}

# Depends on

* [Compliance Recidivism Score (CRS)](/knowledge/compliance-recidivism-score.md)
* [Enforcement Financial Impact Ratio (EFIR)](/knowledge/enforcement-financial-impact-ratio.md)
