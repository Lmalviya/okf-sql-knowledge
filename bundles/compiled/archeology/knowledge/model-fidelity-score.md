---
type: Calculation
title: Model Fidelity Score (MFS)
description: Combines mesh complexity, texture quality, and geometric accuracy to assess overall 3D model fidelity for archaeological analysis.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 6
---

# Definition

MFS = MCR \times \left(\frac{TDI}{10}\right) \times \left(1 + \exp\left(-GeomDeltaMm\right)\right), \text{ where higher values indicate more accurate and detailed models with appropriate complexity.}

# Columns used

* [scanmesh](/tables/scanmesh.md): `geomdeltamm`

# Depends on

* [Mesh Complexity Ratio (MCR)](/knowledge/mesh-complexity-ratio.md)
* [Texture Density Index (TDI)](/knowledge/texture-density-index.md)

# Used by

* [Archaeological Documentation Completeness (ADC)](/knowledge/archaeological-documentation-completeness.md)
* [Digital Preservation Quality (DPQ)](/knowledge/digital-preservation-quality.md)
* [Processing Optimized Workflow](/knowledge/processing-optimized-workflow.md)
