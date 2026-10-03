---
type: Value Illustration
title: messaginganalysis.convnatval
description: Illustrates conversation naturalness value.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 24
---

# Definition

Ranges from 0 to 1. Values above 0.7 indicate natural human conversation, while values below 0.3 suggest automated or scripted responses.

# Columns used

* [messaginganalysis](/tables/messaginganalysis.md): `convnatval`
