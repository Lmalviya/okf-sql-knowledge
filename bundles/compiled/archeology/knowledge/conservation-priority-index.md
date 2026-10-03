---
type: Calculation
title: Conservation Priority Index (CPI)
description: Quantifies the urgency of conservation efforts based on site condition, historical significance and structural stability.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 35
---

# Definition

CPI = \begin{cases} 100 - PS + AF \times \left(1 + \frac{TS}{10}\right), & \text{if in a Degradation Risk Zone} \\ 50 - PS + AF \times \left(1 + \frac{TS}{20}\right), & \text{otherwise} \end{cases}, \text{ where PS is 0-100 based on PresStat condition ('Excellent'=10, 'Good'=30, 'Fair'=50, 'Poor'=70, 'Critical'=90), AF is approximate age in millennia derived from GuessDate, and TS is 0-10 based on TypeSite rarity.}

# Columns used

* [sites](/tables/sites.md): `guessdate`, `typesite`, `presstat`

# Depends on

* [Degradation Risk Zone](/knowledge/degradation-risk-zone.md)
* [GuessDate (Estimated Dating)](/knowledge/guessdate.md)

# Used by

* [Conservation Emergency](/knowledge/conservation-emergency.md)
* [High Temporal Value Site](/knowledge/high-temporal-value-site.md)
