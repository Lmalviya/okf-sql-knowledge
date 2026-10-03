---
type: Value Illustration
title: NoiseDb (Noise Level)
description: Illustrates the impact of noise levels in point cloud data on feature recognition accuracy.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 22
---

# Definition

Measured in decibels, representing signal-to-noise ratio in scan data. Values below 1.0 indicate clean data suitable for detailed analysis, while values above 3.0 suggest significant noise that may obscure small features and introduce measurement uncertainty.

# Columns used

* [scanpointcloud](/tables/scanpointcloud.md): `noisedb`
