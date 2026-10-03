---
type: Value Illustration
title: emerglevel
description: Illustrates the color-coded emergency classification system
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 1
---

# Definition

Yellow indicates monitoring phase with minimal activation, Orange represents partial activation with elevated alert, Red signifies full activation for serious emergencies, and Black denotes critical emergency situations requiring all available resources

# Columns used

* [operations](/tables/operations.md): `emerglevel`

# Used by

* [High-Risk Response Operation](/knowledge/high-risk-response-operation.md)
* [Critical Resource Prioritization Need](/knowledge/critical-resource-prioritization-need.md)
* [Cross-Agency Coordination Crisis](/knowledge/cross-agency-coordination-crisis.md)
