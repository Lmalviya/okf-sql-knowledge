---
type: Calculation
title: Environmental Risk Factor (ERF)
description: Quantifies the overall environmental risk to an artifact based on its sensitivities.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 2
---

# Definition

ERF = \frac{\sum_{i \in sensitivities} SensWeight_i}{|sensitivities|}, \text{where sensitivities includes EnvSensitivity, LightSensitivity, TempSensitivity, etc, with value mapping based on Sensitivity Weight Values.}

# Columns used

* [sensitivitydata](/tables/sensitivitydata.md): `envsensitivity`, `lightsensitivity`, `tempsensitivity`

# Depends on

* [Sensitivity Weight Values](/knowledge/sensitivity-weight-values.md)

# Used by

* [Artifact Vulnerability Score (AVS)](/knowledge/artifact-vulnerability-score.md)
* [Artifact Exhibition Compatibility (AEC)](/knowledge/artifact-exhibition-compatibility.md)
* [Material Deterioration Rate (MDR)](/knowledge/material-deterioration-rate.md)
* [Total Environmental Threat Level (TETL)](/knowledge/total-environmental-threat-level.md)
* [Showcase Protection Adequacy (SPA)](/knowledge/showcase-protection-adequacy.md)
* [Environmental Compliance Index (ECI)](/knowledge/environmental-compliance-index.md)
