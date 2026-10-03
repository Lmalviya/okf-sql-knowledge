---
type: Value Illustration
title: FlowStage (Processing Stage)
description: Illustrates the progression of data processing in archaeological scanning workflows.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 27
---

# Definition

A sequential classification system with defined stages: 'Raw' (unprocessed scan data), 'Aligned' (multiple scans registered together), 'Cleaned' (noise and artifacts removed), 'Meshed' (point cloud converted to polygon mesh), and 'Textured' (surface textures applied to mesh). Each stage represents a discrete processing milestone.

# Columns used

* [scanprocessing](/tables/scanprocessing.md): `flowstage`
