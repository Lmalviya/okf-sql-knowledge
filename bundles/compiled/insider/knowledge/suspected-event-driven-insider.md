---
type: Business Rule
title: Suspected Event-Driven Insider
description: Flags traders identified as event-driven who also trigger potential insider trading alerts.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 41
---

# Definition

A trader who meets the criteria for Event-Driven Trader  AND for whom the Potential Insider Trading Flag  is True.

# Depends on

* [Potential Insider Trading Flag](/knowledge/potential-insider-trading-flag.md)
* [Event-Driven Trader](/knowledge/event-driven-trader.md)
