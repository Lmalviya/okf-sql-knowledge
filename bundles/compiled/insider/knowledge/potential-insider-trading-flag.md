---
type: Business Rule
title: Potential Insider Trading Flag
description: Flags transactions potentially linked to insider knowledge based on timing and context.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 11
---

# Definition

A transaction is flagged if `infoleaksc` > 50.0 AND `corpeventprx` is NOT NULL AND `eventannotm` is 'Pre-market' or 'Intraday'.

# Columns used

* [sentimentandfundamentals](/tables/sentimentandfundamentals.md): `corpeventprx`, `eventannotm`, `infoleaksc`

# Depends on

* [Weighted Investigation Score (WIS)](/knowledge/weighted-investigation-score.md)
* [Sentiment-Weighted Option Volume (SWOV)](/knowledge/sentiment-weighted-option-volume.md)

# Used by

* [Boosted Insider Leakage Score (BILS)](/knowledge/boosted-insider-leakage-score.md)
* [Suspected Event-Driven Insider](/knowledge/suspected-event-driven-insider.md)
* [High-Intensity Insider Investigation](/knowledge/high-intensity-insider-investigation.md)
