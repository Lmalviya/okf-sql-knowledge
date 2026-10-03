---
type: Business Rule
title: Content Farm
description: Identifies accounts mass-producing similar content.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 13
---

# Definition

An account with CMS > 0.7 and postfreq > 50 posts per day

# Columns used

* [contentbehavior](/tables/contentbehavior.md): `postfreq`

# Depends on

* [Content Manipulation Score (CMS)](/knowledge/content-manipulation-score.md)

# Used by

* [Automated Spam Network](/knowledge/automated-spam-network.md)
