---
type: Business Rule
title: Dormant Bot
description: Identifies inactive bot accounts.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 15
---

# Definition

An account with acctstatus = 'Dormant'.

# Columns used

* [account](/tables/account.md): `acctstatus`

# Depends on

* [Bot Behavior Index (BBI)](/knowledge/bot-behavior-index.md)
