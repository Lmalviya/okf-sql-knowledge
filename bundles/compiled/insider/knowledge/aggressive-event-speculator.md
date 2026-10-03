---
type: Business Rule
title: Aggressive Event Speculator
description: Classifies event-driven traders who employ an aggressive risk strategy.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 46
---

# Definition

A trader classified as an Event-Driven Trader  AND whose Trader Risk Appetite  is 'Aggressive'.

# Depends on

* [Event-Driven Trader](/knowledge/event-driven-trader.md)
* [Order Type Distribution](/knowledge/order-type-distribution.md)

# Used by

* [Volatile Event Speculator](/knowledge/volatile-event-speculator.md)
