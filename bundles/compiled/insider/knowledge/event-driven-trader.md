---
type: Business Rule
title: Event-Driven Trader
description: Classifies traders whose activity appears strongly linked to corporate events.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 17
---

# Definition

A trader may be classified as Event-Driven if a significant portion (>30%) of their transactionrecord entries (linked via trdref) have a non-null corpeventprx (joined via transref).

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `trdref`
* [sentimentandfundamentals](/tables/sentimentandfundamentals.md): `transref`, `corpeventprx`
* [compliancecase](/tables/compliancecase.md): `transref`

# Depends on

* [Weighted Investigation Score (WIS)](/knowledge/weighted-investigation-score.md)

# Used by

* [Suspected Event-Driven Insider](/knowledge/suspected-event-driven-insider.md)
* [Aggressive Event Speculator](/knowledge/aggressive-event-speculator.md)
