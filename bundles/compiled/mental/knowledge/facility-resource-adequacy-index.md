---
type: Calculation
title: Facility Resource Adequacy Index (FRAI)
description: Quantifies the adequacy of community resources available at a facility.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 5
---

# Definition

FRAI = \frac{\sum_{i \in facilities} resource\_score_i} {|facilities|}, \text{where } resource\_score = \begin{cases} 3 & \text{if } support\_and\_resources['community\_resources'] = Comprehensive \\ 2 & \text{if } support\_and\_resources['community\_resources'] = Adequate \\ 1 & \text{if } support\_and\_resources['community\_resources'] = Limited \end{cases}, \text{and } support\_and\_resources \text{ is the JSONB column in the facilities table}

# Used by

* [Resource-Supported Facility](/knowledge/resource-supported-facility.md)
* [Resource-Demand Differential (RDD)](/knowledge/resource-demand-differential.md)
* [Socio-Environmental Support Index (SESI)](/knowledge/socio-environmental-support-index.md)
* [High-Need, Under-Resourced Facility](/knowledge/high-need-under-resourced-facility.md)
* [Well-Resourced High-Support Environment](/knowledge/well-resourced-high-support-environment.md)
* [Facility Efficiency Index (FEI)](/knowledge/facility-efficiency-index.md)
* [Correlation Between Resource Adequacy and Adherence (CRAA)](/knowledge/correlation-between-resource-adequacy-and-adherence.md)
