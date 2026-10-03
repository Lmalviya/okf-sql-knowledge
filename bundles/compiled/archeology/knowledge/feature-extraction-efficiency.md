---
type: Calculation
title: Feature Extraction Efficiency (FEE)
description: Measures the efficiency of feature identification in scan data relative to point cloud density and complexity.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 32
---

# Definition

FEE = \frac{TraitCount + ArtiCount}{PCDR \times \sqrt{CloudDense}} \times 10^3, \text{ where PCDR is the Point Cloud Density Ratio and higher values indicate more effective feature extraction from point cloud data relative to spatial distribution efficiency.}

# Columns used

* [scanfeatures](/tables/scanfeatures.md): `traitcount`, `articount`
* [scanpointcloud](/tables/scanpointcloud.md): `clouddense`

# Depends on

* [Point Cloud Density Ratio (PCDR)](/knowledge/point-cloud-density-ratio.md)
