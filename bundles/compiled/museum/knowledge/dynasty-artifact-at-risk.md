---
type: Business Rule
title: Dynasty Artifact at Risk
description: Identifies historically significant dynasty artifacts at conservation risk.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 46
---

# Definition

An artifact that qualifies as a Dynasty Value Artifact AND has a MAP > 3.

# Depends on

* [Dynasty Value Artifact](/knowledge/dynasty-value-artifact.md)
* [Material Aging Projection (MAP)](/knowledge/material-aging-projection.md)
