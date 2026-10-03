---
type: Calculation
title: Mesh-to-Point Ratio (MPR)
description: Evaluates the efficiency of mesh generation from point cloud data for optimal decimation determination.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 36
---

# Definition

MPR = \frac{FacetVerts}{TotalPts} \times 100 \times \left(\frac{MCR}{10}\right)^{0.3}, \text{ where MCR is the Mesh Complexity Ratio and values around 25-30 indicate optimal decimation for archaeological purposes with appropriate feature preservation.}

# Columns used

* [scanmesh](/tables/scanmesh.md): `facetverts`
* [scanpointcloud](/tables/scanpointcloud.md): `totalpts`

# Depends on

* [Mesh Complexity Ratio (MCR)](/knowledge/mesh-complexity-ratio.md)

# Used by

* [Resource-Intensive Model](/knowledge/resource-intensive-model.md)
