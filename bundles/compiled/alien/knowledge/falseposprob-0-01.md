---
type: Value Illustration
title: 'FalsePosProb: <0.01'
description: Illustrates extremely high confidence in signal detection.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 29
---

# Definition

Indicates less than 1% probability that the signal is a false detection or artifact. Such low false positive probability typically results from multiple independent confirmations, excellent signal strength (high $\text{SnrRatio}$), and elimination of all known terrestrial and instrumental sources.

# Columns used

* [signals](/tables/signals.md): `snrratio`
* [signalprobabilities](/tables/signalprobabilities.md): `falseposprob`
