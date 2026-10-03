---
type: Business Rule
title: 'Market Manipulation Pattern: Layering/Spoofing'
description: Identifies trading sessions indicative of layering or spoofing tactics.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 12
---

# Definition

A transaction record suggests Layering/Spoofing if `risk_indicators.layerind` is 'Confirmed' OR (`risk_indicators.spoofprob` > 0.75 AND OMI > 1.0).

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `risk_indicators`

# Depends on

* [Order Modification Intensity (OMI)](/knowledge/order-modification-intensity.md)
* [Combined Manipulation Indicator (CMI)](/knowledge/combined-manipulation-indicator.md)
* [Compliance Health Score (CHS)](/knowledge/compliance-health-score.md)

# Used by

* [Confirmed Manipulator Under Scrutiny](/knowledge/confirmed-manipulator-under-scrutiny.md)
* [High-Risk Manipulator Candidate](/knowledge/high-risk-manipulator-candidate.md)
* [Confirmed Evasive Layering/Spoofing](/knowledge/confirmed-evasive-layering-spoofing.md)
