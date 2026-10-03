---
type: Business Rule
title: Volatile Event Speculator
description: Flags aggressive event speculators whose trading coincides with high sentiment divergence, indicating potential reaction to conflicting information.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 64
---

# Definition

A trader identified as an Aggressive Event Speculator  AND associated with a high Sentiment Divergence Factor (e.g., SDF > 1.0).

# Depends on

* [Sentiment Divergence Factor (SDF)](/knowledge/sentiment-divergence-factor.md)
* [Aggressive Event Speculator](/knowledge/aggressive-event-speculator.md)
