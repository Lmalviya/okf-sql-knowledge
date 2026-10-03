---
type: Business Rule
title: Habitable Zone Transmission
description: Identifies signals originating from stellar habitable zones with technological characteristics.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 41
---

# Definition

A signal with $\text{HZSR} > 1.5$ and Technosignature characteristics, originating from a star system with conditions potentially suitable for life, making it a priority candidate for SETI research.

# Depends on

* [Technosignature](/knowledge/technosignature.md)
* [Habitable Zone Signal Relevance (HZSR)](/knowledge/habitable-zone-signal-relevance.md)
