---
type: Business Rule
title: Potentially Evasive Order Modifier
description: Flags high cancellation/modification traders who make significant use of dark pools.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 47
---

# Definition

A trader identified as a High Cancellation/Modification Trader  AND whose transaction records show Dark Pool Usage  in more than 50% of instances.

# Depends on

* [High Cancellation/Modification Trader](/knowledge/high-cancellation-modification-trader.md)
* [Dark Pool Usage Venues](/knowledge/dark-pool-usage-venues.md)
