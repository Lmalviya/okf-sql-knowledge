---
type: Value Illustration
title: GeomDeltaMm (Geometric Accuracy)
description: Illustrates the significance of geometric accuracy in 3D models for measurement reliability.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 24
---

# Definition

Measured in millimeters, representing the average deviation between the scan data and final 3D model. Values below 0.1mm indicate museum-quality accuracy, while values around 1.0mm are suitable for general documentation but introduce uncertainty in fine feature analysis.

# Columns used

* [scanmesh](/tables/scanmesh.md): `geomdeltamm`
