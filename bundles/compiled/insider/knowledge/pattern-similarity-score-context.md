---
type: Value Illustration
title: Pattern Similarity Score Context
description: Provides context for the pattern similarity score, comparing trading to known illicit behaviors.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 28
---

# Definition

`patsim`: A score typically ranging from 0 to 1. Values close to 1 indicate a high similarity to known illicit trading patterns cataloged by the surveillance system (e.g., layering, spoofing, wash trading). Values close to 0 indicate the observed trading patterns do not strongly match known manipulative techniques.

# Columns used

* [advancedbehavior](/tables/advancedbehavior.md): `patsim`

# Used by

* [Unique Pattern Deviation Ratio (UPDR)](/knowledge/unique-pattern-deviation-ratio.md)
