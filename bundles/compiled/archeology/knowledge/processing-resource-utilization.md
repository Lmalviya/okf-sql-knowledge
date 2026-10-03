---
type: Calculation
title: Processing Resource Utilization (PRU)
description: Measures the efficiency of computing resource utilization during scan processing relative to data complexity.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 37
---

# Definition

PRU = \frac{FlowHrs \times (ProcCPU + ProcGPU) / 2}{GBSize \times 10 \times \log_{10}(FacetVerts + 10^4)}, \text{ where lower values indicate more efficient use of computing resources relative to mesh complexity.}

# Columns used

* [scanmesh](/tables/scanmesh.md): `facetverts`
* [scanprocessing](/tables/scanprocessing.md): `flowhrs`, `proccpu`, `procgpu`
* [scans](/tables/scans.md): `gbsize`

# Used by

* [Processing Optimized Workflow](/knowledge/processing-optimized-workflow.md)
* [Workflow Efficiency Classification](/knowledge/workflow-efficiency-classification.md)
