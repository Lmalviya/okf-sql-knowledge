---
type: Business Rule
title: Workflow Efficiency Classification
description: A standardized categorization system for assessing processing workflow efficiency based on Processing Resource Utilization (PRU) values.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 51
---

# Definition

A three-tier classification where 'Optimized' workflows have PRU < 5.0 (highly efficient resource usage), 'Acceptable' workflows have PRU between 5.0-10.0 (reasonable efficiency), and 'Needs Optimization' workflows have PRU > 10.0 (inefficient resource usage requiring intervention). This classification guides processing workflow improvements and resource allocation decisions.

# Depends on

* [Processing Resource Utilization (PRU)](/knowledge/processing-resource-utilization.md)
