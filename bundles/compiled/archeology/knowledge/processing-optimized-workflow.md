---
type: Business Rule
title: Processing Optimized Workflow
description: Defines optimized processing workflows balancing quality and resource use through benchmarked performance metrics.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 43
---

# Definition

A processing workflow with PRU < 5.0 while maintaining MFS > 7.0, where PRU is Processing Resource Utilization and MFS is Model Fidelity Score, representing an efficient balance of resource use and output quality through optimized algorithm selection and hardware allocation.

# Depends on

* [Processing Resource Utilization (PRU)](/knowledge/processing-resource-utilization.md)
* [Model Fidelity Score (MFS)](/knowledge/model-fidelity-score.md)
