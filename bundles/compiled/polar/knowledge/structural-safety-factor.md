---
type: Calculation
title: Structural Safety Factor (SSF)
description: Evaluates the safety margin of structures under extreme weather conditions.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 3
---

# Definition

SSF = \frac{100 - structuralloadpercent}{100} \times \begin{cases} 0.5 & \text{if snowloadkgm2 > 100 or windspeedms > 20} \\ 0.8 & \text{if snowloadkgm2 > 50 or windspeedms > 10} \\ 1.0 & \text{otherwise} \end{cases}

# Columns used

* [weatherandstructure](/tables/weatherandstructure.md): `windspeedms`, `snowloadkgm2`, `structuralloadpercent`

# Used by

* [Extreme Weather Readiness (EWR)](/knowledge/extreme-weather-readiness.md)
* [Extreme Climate Adaptation Coefficient (ECAC)](/knowledge/extreme-climate-adaptation-coefficient.md)
* [Extreme Operating Conditions (EOC)](/knowledge/extreme-operating-conditions.md)
* [Critical Infrastructure Protection Level (CIPL)](/knowledge/critical-infrastructure-protection-level.md)
* [Extreme Weather Readiness Status (EWRS)](/knowledge/extreme-weather-readiness-status.md)
