---
type: Business Rule
title: Comprehensive Coverage
description: Defines the standard for comprehensive scan coverage of an archaeological site or artifact with statistical confidence.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 11
---

# Definition

A scan with CoverPct \geq 95 and LapPct \geq 30, ensuring minimal data gaps and sufficient overlap for accurate registration with 95% confidence interval for spatial measurements.

# Columns used

* [scanpointcloud](/tables/scanpointcloud.md): `coverpct`, `lappct`

# Used by

* [Premium Quality Scan](/knowledge/premium-quality-scan.md)
