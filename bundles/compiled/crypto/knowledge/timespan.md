---
type: Value Illustration
title: timespan
description: Illustrates the meaning of different values for the timespan enum.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 22
---

# Definition

An enum with values 'IOC', 'GTC', 'GTD', or 'FOK'. 'IOC' (Immediate-or-Cancel) means execute immediately available portion or cancel. 'GTC' (Good-Till-Cancelled) means the order remains active until explicitly cancelled. 'GTD' (Good-Till-Date) means the order remains active until a specified date. 'FOK' (Fill-or-Kill) means execute completely immediately or cancel entirely.

# Columns used

* [orders](/tables/orders.md): `timespan`
