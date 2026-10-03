---
type: Calculation
title: Mesh Complexity Ratio (MCR)
description: Measures the topological complexity of a mesh relative to its resolution, helping identify overly complex or simplified archaeological models.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 4
---

# Definition

MCR = \frac{FacetFaces}{FacetVerts \times FacetResMm^2} \times 10^3, \text{ where higher values indicate more complex meshes for a given resolution, capturing finer archaeological details.}

# Columns used

* [scanmesh](/tables/scanmesh.md): `facetverts`, `facetfaces`, `facetresmm`

# Used by

* [Model Fidelity Score (MFS)](/knowledge/model-fidelity-score.md)
* [High Fidelity Mesh](/knowledge/high-fidelity-mesh.md)
* [Mesh-to-Point Ratio (MPR)](/knowledge/mesh-to-point-ratio.md)
