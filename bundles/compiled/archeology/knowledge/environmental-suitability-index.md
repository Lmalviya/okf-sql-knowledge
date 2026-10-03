---
type: Calculation
title: Environmental Suitability Index (ESI)
description: Evaluates how suitable environmental conditions were for scanning operations using weighted parameters.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 7
---

# Definition

ESI = 100 - 2.5 \times \left|AmbicTemp - 20\right| - \left|\frac{HumePct - 50}{2}\right|^{1.5} - \frac{600}{IllumeLux + 100}, \text{ where higher values indicate more ideal scanning conditions adjusted for relative importance.}

# Columns used

* [scanenvironment](/tables/scanenvironment.md): `ambictemp`, `humepct`, `illumelux`

# Used by

* [Optimal Scanning Conditions](/knowledge/optimal-scanning-conditions.md)
* [Environmental Impact Factor (EIF)](/knowledge/environmental-impact-factor.md)
* [Equipment Optimization Opportunity](/knowledge/equipment-optimization-opportunity.md)
* [Environmental Condition Classification System (ECCS)](/knowledge/environmental-condition-classification-system.md)
