---
type: Value Illustration
title: Trader Position Holding Style
description: Illustrates the typical duration traders hold their positions, based on their strategy.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 20
---

# Definition

`posspan`: 'Intraday' implies positions are typically opened and closed within the same trading day. 'Swing' suggests holding for a few days to weeks, capturing short-term price moves. 'Position' implies holding for weeks to months, based on broader trends. 'Long-term' indicates holding for months or years, often based on fundamental analysis.

# Columns used

* [trader](/tables/trader.md): `posspan`
