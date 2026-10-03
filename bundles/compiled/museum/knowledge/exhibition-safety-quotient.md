---
type: Calculation
title: Exhibition Safety Quotient (ESQ)
description: Comprehensive safety rating for an exhibition based on artifacts, showcases, and visitor factors.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 35
---

# Definition

ESQ = ((10 - AVS) + AEC + (10 - VIR)) ÷ 3, where AVS is the Artifact Vulnerability Score, AEC is the Artifact Exhibition Compatibility, and VIR is the Visitor Impact Risk. Higher values indicate safer exhibitions.

# Depends on

* [Artifact Vulnerability Score (AVS)](/knowledge/artifact-vulnerability-score.md)
* [Artifact Exhibition Compatibility (AEC)](/knowledge/artifact-exhibition-compatibility.md)
* [Visitor Impact Risk (VIR)](/knowledge/visitor-impact-risk.md)
