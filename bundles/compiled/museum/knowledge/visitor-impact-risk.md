---
type: Calculation
title: Visitor Impact Risk (VIR)
description: Assesses the risk posed by visitor traffic to artifacts in exhibition halls.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 10
---

# Definition

VIR = \frac{VisitorCountDaily \times VisitorFlowRate \times VisitorDwellMin}{1000}, \text{where VisitorFlowRate is numerically mapped: Low=1, Medium=3, High=5}

# Columns used

* [exhibitionhalls](/tables/exhibitionhalls.md): `visitorcountdaily`, `visitorflowrate`, `visitordwellmin`

# Used by

* [Visitor Crowd Risk](/knowledge/visitor-crowd-risk.md)
* [Visitor Capacity Safety Factor (VCSF)](/knowledge/visitor-capacity-safety-factor.md)
* [Exhibition Safety Quotient (ESQ)](/knowledge/exhibition-safety-quotient.md)
* [Security Risk Exposure (SRE)](/knowledge/security-risk-exposure.md)
