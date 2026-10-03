---
type: Business Rule
title: High-Confidence Technosignature
description: Defines signals with extremely high likelihood of technological origin.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 40
---

# Definition

A Technosignature with $\text{CCS} > 0.9$, $\text{MCS} > 1.5$, and $\text{AIDP} > 0.8$, indicating a signal that meets the basic Technosignature criteria with additional confirmation through modulation complexity and artificial intelligence detection markers.

# Depends on

* [Technosignature](/knowledge/technosignature.md)
* [Modulation Complexity Score (MCS)](/knowledge/modulation-complexity-score.md)
* [Artificial Intelligence Detection Probability (AIDP)](/knowledge/artificial-intelligence-detection-probability.md)
* [Confirmation Confidence Score (CCS)](/knowledge/confirmation-confidence-score.md)
