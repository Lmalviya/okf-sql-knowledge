---
type: Business Rule
title: Premium Quality Scan
description: Defines the criteria for a premium quality archaeological scan suitable for conservation planning and scholarly publication.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 12
---

# Definition

A scan that is both a High Resolution Scan and has Comprehensive Coverage with SQS > 7.5, where SQS is the Scan Quality Score, producing data suitable for detailed analysis and conservation planning.

# Depends on

* [High Resolution Scan](/knowledge/high-resolution-scan.md)
* [Comprehensive Coverage](/knowledge/comprehensive-coverage.md)
* [Scan Quality Score (SQS)](/knowledge/scan-quality-score.md)

# Used by

* [Digital Conservation Priority](/knowledge/digital-conservation-priority.md)
* [Full Archaeological Digital Twin](/knowledge/full-archaeological-digital-twin.md)
