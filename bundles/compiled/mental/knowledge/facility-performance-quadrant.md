---
type: Business Rule
title: Facility Performance Quadrant (FPQ)
description: Categorizes facilities into performance quadrants based on their Treatment Adherence Rate and Patient Stability Metric relative to median thresholds.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 61
---

# Definition

A facility is assigned to one of four quadrants: 'High Adherence, High Stability' if TAR ≥ median_tar and PSM ≥ median_psm; 'High Adherence, Low Stability' if TAR ≥ median_tar and PSM < median_psm; 'Low Adherence, High Stability' if TAR < median_tar and PSM ≥ median_psm; 'Low Adherence, Low Stability' if TAR < median_tar and PSM < median_psm.

# Depends on

* [Treatment Adherence Rate (TAR)](/knowledge/treatment-adherence-rate.md)
* [Patient Stability Metric (PSM)](/knowledge/patient-stability-metric.md)
