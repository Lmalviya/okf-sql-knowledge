---
type: Calculation
title: Boosted Insider Leakage Score (BILS)
description: Increases the Information Leakage Score if a Potential Insider Trading Flag is also present.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 38
---

# Definition

BILS = \text{InfoLeakageScoreValue} \times (1.5 \text{ if Potential Insider Trading Flag  is True else } 1.0) \\ \text{where InfoLeakageScoreValue is from Information Leakage Score Interpretation .}

# Depends on

* [Potential Insider Trading Flag](/knowledge/potential-insider-trading-flag.md)
* [Information Leakage Score Interpretation](/knowledge/information-leakage-score-interpretation.md)

# Used by

* [Significant Enforcement Action](/knowledge/significant-enforcement-action.md)
* [Insider Sentiment Short Ratio (ISSR)](/knowledge/insider-sentiment-short-ratio.md)
