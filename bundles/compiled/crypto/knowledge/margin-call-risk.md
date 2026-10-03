---
type: Business Rule
title: Margin Call Risk
description: Identifies accounts at risk of receiving a margin call.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 18
---

# Definition

Accounts where the Margin Utilization exceeds 80%, putting them at risk of margin calls if market prices move adversely.

# Depends on

* [Margin Utilization](/knowledge/margin-utilization.md)

# Used by

* [Critically Over-Leveraged Position](/knowledge/critically-over-leveraged-position.md)
