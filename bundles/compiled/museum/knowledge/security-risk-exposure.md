---
type: Calculation
title: Security Risk Exposure (SRE)
description: Quantifies an artifact's exposure to security risks based on value and security measures.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 40
---

# Definition

SRE = (InsValueUSD ÷ 100000) × (10 - VIR) ÷ 10, where VIR is the Visitor Impact Risk. Higher values indicate greater security risk exposure.

# Columns used

* [artifactsecurityaccess](/tables/artifactsecurityaccess.md): `insvalueusd`

# Depends on

* [Visitor Impact Risk (VIR)](/knowledge/visitor-impact-risk.md)

# Used by

* [High Security Priority Artifact](/knowledge/high-security-priority-artifact.md)
