---
type: Business Rule
title: High Fidelity Mesh
description: Defines criteria for high-fidelity 3D mesh models in archaeological documentation suitable for analytical studies.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 13
---

# Definition

A mesh with MCR > 5.0, FacetResMm < 1.0, and GeomDeltaMm < 0.5, where MCR is the Mesh Complexity Ratio, capable of representing fine archaeological details and surface morphology.

# Columns used

* [scanmesh](/tables/scanmesh.md): `facetresmm`, `geomdeltamm`

# Depends on

* [Mesh Complexity Ratio (MCR)](/knowledge/mesh-complexity-ratio.md)

# Used by

* [Full Archaeological Digital Twin](/knowledge/full-archaeological-digital-twin.md)
* [Mesh Quality Classification](/knowledge/mesh-quality-classification.md)
