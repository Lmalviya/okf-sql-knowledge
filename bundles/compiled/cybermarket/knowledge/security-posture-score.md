---
type: Calculation
title: Security Posture Score (SPS)
description: Evaluates the overall security posture of an entity
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 17
---

# Definition

SPS = (100 - (vulntally \times 5)) + (securitymeasurecount \times 2) + (sessionsecurityscore \times 0.5) + (privprotscore \times 0.3) - (fpprob \times 100), \text{where higher scores indicate stronger security postures.}

# Columns used

* [securitymonitoring](/tables/securitymonitoring.md): `vulntally`, `securitymeasurecount`, `sessionsecurityscore`, `privprotscore`, `fpprob`

# Used by

* [High-Security Entity](/knowledge/high-security-entity.md)
* [Operational Security Index (OSI)](/knowledge/operational-security-index.md)
