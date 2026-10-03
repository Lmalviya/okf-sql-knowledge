---
type: Business Rule
title: Multi-Phase Documentation Project
description: Defines complex archaeological projects requiring multiple scanning phases with integrated documentation strategy.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 48
---

# Definition

A project with multiple scans where the total ADC < 70 for individual scans but DPQ > 80 when combined, where ADC is Archaeological Documentation Completeness and DPQ is Digital Preservation Quality, indicating comprehensive documentation achieved through multiple phases with coherent registration strategy for holistic interpretation.

# Depends on

* [Archaeological Documentation Completeness (ADC)](/knowledge/archaeological-documentation-completeness.md)
* [Digital Preservation Quality (DPQ)](/knowledge/digital-preservation-quality.md)
