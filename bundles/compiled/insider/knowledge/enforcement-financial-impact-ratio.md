---
type: Calculation
title: Enforcement Financial Impact Ratio (EFIR)
description: Calculates the ratio of the penalty amount to the trader's account balance at the time of the related transaction.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 9
---

# Definition

EFIR = \frac{\text{penamt}}{\text{acctbal}}

# Columns used

* [trader](/tables/trader.md): `acctbal`
* [enforcementactions](/tables/enforcementactions.md): `penamt`

# Used by

* [Logarithmic Enforcement Fine Impact (LEFI)](/knowledge/logarithmic-enforcement-fine-impact.md)
* [Financially Impactful Enforcement Case](/knowledge/financially-impactful-enforcement-case.md)
* [Recidivism Enforcement Severity (RES)](/knowledge/recidivism-enforcement-severity.md)
