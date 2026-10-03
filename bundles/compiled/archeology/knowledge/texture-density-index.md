---
type: Calculation
title: Texture Density Index (TDI)
description: Evaluates the pixel density of textures relative to mesh resolution for assessing surface detail preservation.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 5
---

# Definition

TDI = \frac{TexPix}{\sqrt{FacetFaces} \times FacetResMm} \times 10^{-2}, \text{ where higher values indicate more detailed textures relative to geometric complexity.}

# Columns used

* [scanmesh](/tables/scanmesh.md): `facetfaces`, `facetresmm`, `texpix`

# Used by

* [Model Fidelity Score (MFS)](/knowledge/model-fidelity-score.md)
* [Texture-Critical Artifact](/knowledge/texture-critical-artifact.md)
