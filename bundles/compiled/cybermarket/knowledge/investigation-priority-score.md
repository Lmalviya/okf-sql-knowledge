---
type: Calculation
title: Investigation Priority Score (IPS)
description: Determines how urgently an investigation should be handled
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 18
---

# Definition

IPS = (lawinterest\_numeric \times 30) + (regrisklvl\_numeric \times 20) + (fraudprob \times 100) - (compliancescore \times 0.5) + (notescount \times 2), \text{where lawinterest\_numeric and regrisklvl\_numeric map Low=1, Medium=2, High=3, Unknown=2, and higher scores indicate higher priority.}

# Columns used

* [investigation](/tables/investigation.md): `lawinterest`, `regrisklvl`, `compliancescore`, `notescount`
* [riskanalysis](/tables/riskanalysis.md): `fraudprob`

# Used by

* [Priority Investigation Target](/knowledge/priority-investigation-target.md)
