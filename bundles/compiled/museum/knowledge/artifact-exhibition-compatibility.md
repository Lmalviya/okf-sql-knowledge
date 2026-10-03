---
type: Calculation
title: Artifact Exhibition Compatibility (AEC)
description: Determines how compatible an artifact is with its current showcase environment.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 6
---

# Definition

AEC = 10 - |ERF - SESR|, \text{where a score closer to 10 indicates better compatibility}

# Depends on

* [Environmental Risk Factor (ERF)](/knowledge/environmental-risk-factor.md)
* [Showcase Environmental Stability Rating (SESR)](/knowledge/showcase-environmental-stability-rating.md)

# Used by

* [Exhibition Safety Quotient (ESQ)](/knowledge/exhibition-safety-quotient.md)
