---
type: Business Rule
title: Content Preference Classification
description: Categorizes fans based on their primary content consumption preferences
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 51
---

# Definition

Uses the contpref field to classify viewers: contpref = 'Music' maps to 'Content Consumer (Music)', contpref = 'Dance' maps to 'Content Consumer (Dance)', contpref = 'Gaming' maps to 'Content Consumer (Gaming)', and all other values map to 'General Content Consumer'. This classification enables targeted content delivery and personalized marketing.

# Columns used

* [engagement](/tables/engagement.md): `contpref`
