---
type: Value Illustration
title: ArtifactsCore.ConserveStatus
description: Illustrates the conservation status values and their meanings.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 21
---

# Definition

Values range from 'Excellent' (recently conserved, no issues), 'Good' (stable with minor issues), 'Fair' (stable but with noticeable issues), 'Poor' (active deterioration), to 'Critical' (severe deterioration requiring immediate intervention).

# Columns used

* [artifactscore](/tables/artifactscore.md): `conservestatus`

# Used by

* [Light Exposure Thresholds](/knowledge/light-exposure-thresholds.md)
