---
type: Calculation
title: Market Impact Cost (MIC)
description: Estimates the market impact cost of executing a large order.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 4
---

# Definition

MIC = dealcount \times dealquote \times mkteffect \times 0.01, \text{where } dealcount \text{ is the order quantity, } dealquote \text{ is the limit or stop price, and } mkteffect \text{ is the approximating internal market impact.}

# Columns used

* [orders](/tables/orders.md): `dealquote`, `dealcount`
* [systemmonitoring](/tables/systemmonitoring.md): `mkteffect`
