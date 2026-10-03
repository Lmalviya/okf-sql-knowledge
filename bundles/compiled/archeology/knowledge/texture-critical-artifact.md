---
type: Business Rule
title: Texture-Critical Artifact
description: Identifies artifacts where texture documentation is critical for analysis based on surface morphology characteristics.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 41
---

# Definition

Features with TextureStudy containing 'Detailed' or 'Critical' and TDI > 8.0, where TDI is the Texture Density Index, requiring specialized imaging techniques such as photometric stereo or multi-spectral imaging for complete surface characterization.

# Columns used

* [scanfeatures](/tables/scanfeatures.md): `texturestudy`

# Depends on

* [Texture Density Index (TDI)](/knowledge/texture-density-index.md)
