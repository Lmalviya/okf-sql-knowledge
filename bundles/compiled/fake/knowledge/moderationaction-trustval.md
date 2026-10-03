---
type: Value Illustration
title: moderationaction.trustval
description: Illustrates trust value meaning.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 27
---

# Definition

Ranges from 0 to 1. Values above 0.7 indicate highly trusted accounts, while values below 0.3 suggest untrusted or suspicious accounts.

# Columns used

* [moderationaction](/tables/moderationaction.md): `trustval`
