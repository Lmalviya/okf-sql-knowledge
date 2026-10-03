---
type: Business Rule
title: Observation-Verified Signal
description: Defines signals that have undergone rigorous verification processes.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 48
---

# Definition

Signals observed under Optimal Observing Window (OOW) conditions with $\text{OQF} > 0.85$ and $\text{CCS} > 0.8$, indicating high-quality observations with multiple verification methods applied.

# Depends on

* [Optimal Observing Window (OOW)](/knowledge/optimal-observing-window.md)
* [Observation Quality Factor (OQF)](/knowledge/observation-quality-factor.md)
* [Confirmation Confidence Score (CCS)](/knowledge/confirmation-confidence-score.md)
