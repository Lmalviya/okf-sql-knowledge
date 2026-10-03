---
type: Calculation
title: Information Entropy Ratio (IER)
description: Compares signal entropy to expected natural background entropy.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 33
---

# Definition

$\text{IER} = \frac{\text{EntropyVal}}{\text{NatSrcProb} \times 0.9 + 0.1}$, where values significantly greater than 1 suggest non-natural information content. Uses NatSrcProb as a baseline for expected natural entropy.

# Columns used

* [signalprobabilities](/tables/signalprobabilities.md): `natsrcprob`
* [signalclassification](/tables/signalclassification.md): `entropyval`
