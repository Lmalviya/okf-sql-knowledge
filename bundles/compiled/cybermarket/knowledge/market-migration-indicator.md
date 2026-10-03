---
type: Business Rule
title: Market Migration Indicator
description: Identifies signs of users migrating between markets
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 27
---

# Definition

A pattern where multiple vendors (vendregistry) and buyers (buyregistry) associated with one market (mktregistry) begin appearing on another market within a short timeframe (less than 30 days), often following security incidents or market instability. These migrations typically indicate market disruption events requiring adjustments to monitoring priorities.

# Columns used

* [markets](/tables/markets.md): `mktregistry`
* [vendors](/tables/vendors.md): `vendregistry`
* [buyers](/tables/buyers.md): `buyregistry`
