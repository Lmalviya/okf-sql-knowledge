---
type: Calculation
title: Spatial Density Index (SDI)
description: Assesses point cloud density relative to site dimensions for spatial sampling adequacy.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 34
---

# Definition

SDI = \frac{TotalPts}{AreaM2 \times 10^4} \times \left(\frac{PointDense}{CloudDense}\right)^{0.5}

# Columns used

* [scanspatial](/tables/scanspatial.md): `aream2`
* [scanpointcloud](/tables/scanpointcloud.md): `pointdense`, `totalpts`, `clouddense`

# Used by

* [Spatially Complex Site](/knowledge/spatially-complex-site.md)
