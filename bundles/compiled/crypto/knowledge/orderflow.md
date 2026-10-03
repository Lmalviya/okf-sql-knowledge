---
type: Value Illustration
title: orderflow
description: Illustrates the meaning of different values for the orderflow enum.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 21
---

# Definition

An enum with values 'New', 'PartiallyFilled', 'Cancelled', or 'Filled'. 'New' indicates a newly placed order that hasn't been matched. 'PartiallyFilled' means some portion has been executed but not all. 'Cancelled' means the order was cancelled before full execution. 'Filled' means the order has been completely executed.

# Columns used

* [orders](/tables/orders.md): `orderflow`
