---
type: Value Illustration
title: dealedge
description: Illustrates the meaning of different values for the dealedge enum.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 20
---

# Definition

An enum with values 'Buy' or 'Sell'. 'Buy' indicates the order is to purchase the base asset using the quote asset (e.g., buying BTC with USDT). 'Sell' indicates the order is to sell the base asset for the quote asset (e.g., selling BTC for USDT).

# Columns used

* [orders](/tables/orders.md): `dealedge`
