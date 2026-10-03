---
type: Business Rule
title: Critically Over-Leveraged Position
description: Identifies positions with extremely dangerous leverage levels requiring immediate risk management.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 40
---

# Definition

A position that qualifies as an Over-Leveraged Position where additionally the Effective Leverage exceeds 20 and the Margin Utilization exceeds 90%, creating extreme liquidation risk.

# Depends on

* [Over-Leveraged Position](/knowledge/over-leveraged-position.md)
* [Effective Leverage](/knowledge/effective-leverage.md)
* [Margin Call Risk](/knowledge/margin-call-risk.md)
