---
type: Calculation
title: Aggressive Suspicion Score (ASS)
description: Combines overall suspicious activity index with aggressive trading intensity, identifying traders who are both suspicious and trade aggressively.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 54
---

# Definition

ASS = \text{SAI} \times \text{ATI}

# Depends on

* [Suspicious Activity Index (SAI)](/knowledge/suspicious-activity-index.md)
* [Aggressive Trading Intensity (ATI)](/knowledge/aggressive-trading-intensity.md)
