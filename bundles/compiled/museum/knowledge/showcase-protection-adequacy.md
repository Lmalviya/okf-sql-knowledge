---
type: Calculation
title: Showcase Protection Adequacy (SPA)
description: Measures how well a showcase protects its artifacts based on its stability and the artifacts' requirements.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 32
---

# Definition

SPA = SESR - (ERF × 0.5), where SESR is the Showcase Environmental Stability Rating and ERF is the Environmental Risk Factor. Positive values indicate adequate protection.

# Depends on

* [Showcase Environmental Stability Rating (SESR)](/knowledge/showcase-environmental-stability-rating.md)
* [Environmental Risk Factor (ERF)](/knowledge/environmental-risk-factor.md)

# Used by

* [Showcase Compatibility Issue](/knowledge/showcase-compatibility-issue.md)
