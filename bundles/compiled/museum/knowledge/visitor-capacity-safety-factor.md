---
type: Calculation
title: Visitor Capacity Safety Factor (VCSF)
description: Determines the safe visitor capacity for exhibition halls containing sensitive artifacts.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 34
---

# Definition

VCSF = VIR ÷ (AVS × 0.1), where VIR is the Visitor Impact Risk and AVS is the Artifact Vulnerability Score. Lower values indicate safer visitor capacities.

# Depends on

* [Visitor Impact Risk (VIR)](/knowledge/visitor-impact-risk.md)
* [Artifact Vulnerability Score (AVS)](/knowledge/artifact-vulnerability-score.md)

# Used by

* [Visitor Traffic Safety Concern](/knowledge/visitor-traffic-safety-concern.md)
