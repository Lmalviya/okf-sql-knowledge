---
type: Value Illustration
title: moderationaction.impactval
description: Illustrates impact value meaning.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 28
---

# Definition

Ranges from 0 to 1. Values above 0.7 indicate high-impact violations requiring immediate attention, while values below 0.3 suggest low-priority issues.

# Columns used

* [moderationaction](/tables/moderationaction.md): `impactval`
