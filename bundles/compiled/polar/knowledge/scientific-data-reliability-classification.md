---
type: Business Rule
title: Scientific Data Reliability Classification
description: Classifies scientific data based on equipment reliability and calibration status.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 16
---

# Definition

Scientific data is classified as 'Research Grade' when collected by equipment with SER > 0.9, with valid calibration status, and under appropriate environmental conditions for the equipment type.

# Depends on

* [Scientific Equipment Reliability (SER)](/knowledge/scientific-equipment-reliability.md)
