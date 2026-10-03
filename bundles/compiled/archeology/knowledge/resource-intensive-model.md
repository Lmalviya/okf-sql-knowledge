---
type: Business Rule
title: Resource-Intensive Model
description: Identifies 3D models requiring substantial computing resources for visualization and analysis based on complexity metrics.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 47
---

# Definition

A model with FacetFaces > 2,000,000 and MPR < 15, where MPR is Mesh-to-Point Ratio, requiring specialized hardware for effective interaction and analytical software optimized for large-scale geometric processing with hierarchical level-of-detail implementation.

# Columns used

* [scanmesh](/tables/scanmesh.md): `facetfaces`

# Depends on

* [Mesh-to-Point Ratio (MPR)](/knowledge/mesh-to-point-ratio.md)
