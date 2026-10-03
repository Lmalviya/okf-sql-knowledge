---
type: Business Rule
title: Organic Material Emergency
description: Identifies emergency situations for organic materials.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 50
---

# Definition

Occurs when an artifact falls under the Organic Material Vulnerability classification AND has a TETL > 12.

# Depends on

* [Organic Material Vulnerability](/knowledge/organic-material-vulnerability.md)
* [Total Environmental Threat Level (TETL)](/knowledge/total-environmental-threat-level.md)
