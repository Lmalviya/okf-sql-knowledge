---
type: Calculation
title: Insider Sentiment Short Ratio (ISSR)
description: Combines boosted insider leakage score with relative short interest, identifying potential insider trading concurrent with high relative short interest.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 58
---

# Definition

ISSR = \text{BILS} \times \text{RSI} \\ \text{where BILS is Boosted Insider Leakage Score  and RSI is Relative Short Interest .}

# Depends on

* [Relative Short Interest (RSI)](/knowledge/relative-short-interest.md)
* [Boosted Insider Leakage Score (BILS)](/knowledge/boosted-insider-leakage-score.md)
