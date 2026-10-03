---
type: Calculation
title: Weighted Investigation Score (WIS)
description: Combines raw investigation scores with the current alert severity level.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 33
---

# Definition

WIS = \text{III} \times \text{AlertLevelMultiplier} \\ \text{where III is Investigation Intensity Index } \\ \text{and AlertLevelMultiplier maps Alert Level Severity  to numeric: 'Low'=1, 'Medium'=2, 'High'=3, 'Critical'=4.}

# Depends on

* [Investigation Intensity Index (III)](/knowledge/investigation-intensity-index.md)
* [Logarithmic Enforcement Fine Impact (LEFI)](/knowledge/logarithmic-enforcement-fine-impact.md)

# Used by

* [Potential Insider Trading Flag](/knowledge/potential-insider-trading-flag.md)
* [Event-Driven Trader](/knowledge/event-driven-trader.md)
* [Investigation Compliance Risk Index (ICRI)](/knowledge/investigation-compliance-risk-index.md)
