---
type: Business Rule
title: Whale-Driven Market
description: Identifies periods where large traders significantly influence price direction.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 46
---

# Definition

Market conditions where whalemotion is 'High' and there is at least one Whale Order in the same direction as the Smart Money Flow, indicating coordinated activity among large market participants.

# Depends on

* [Whale Order](/knowledge/whale-order.md)
* [Smart Money Flow](/knowledge/smart-money-flow.md)
* [whalemotion](/knowledge/whalemotion.md)
