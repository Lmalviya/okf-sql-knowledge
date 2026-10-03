---
type: Calculation
title: Water Resource Management Index (WRMI)
description: Evaluates the efficiency of water resource management based on water levels, quality, and waste levels.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 7
---

# Definition

WRMI = waterlevelpercent \times \frac{waterqualityindex}{100} \times (1 - \frac{wastetanklevelpercent}{100}), \text{ where higher water quality and appropriate water/waste levels indicate better management.}

# Columns used

* [waterandwaste](/tables/waterandwaste.md): `waterlevelpercent`, `waterqualityindex`, `wastetanklevelpercent`

# Used by

* [Water Conservation Requirement](/knowledge/water-conservation-requirement.md)
* [Resource Self-Sufficiency Index (RSSI)](/knowledge/resource-self-sufficiency-index.md)
* [Energy-Water Resource Integration Index (EWRII)](/knowledge/energy-water-resource-integration-index.md)
* [Water Resource Management Status Classification (WRMSC)](/knowledge/water-resource-management-status-classification.md)
