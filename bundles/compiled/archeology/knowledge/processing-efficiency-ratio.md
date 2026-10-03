---
type: Calculation
title: Processing Efficiency Ratio (PER)
description: Measures the efficiency of scan processing by comparing processing time to data complexity and size.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 8
---

# Definition

PER = \frac{GBSize \times \log_{10}(TotalPts)}{FlowHrs \times (ProcCPU + ProcGPU)/200}, \text{ where higher values indicate more efficient processing relative to data complexity.}

# Columns used

* [scanprocessing](/tables/scanprocessing.md): `flowhrs`, `proccpu`, `procgpu`
* [scans](/tables/scans.md): `gbsize`
* [scanpointcloud](/tables/scanpointcloud.md): `totalpts`

# Used by

* [Processing Bottleneck](/knowledge/processing-bottleneck.md)
