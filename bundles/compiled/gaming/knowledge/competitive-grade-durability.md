---
type: Business Rule
title: Competitive-Grade Durability
description: Defines durability standards for devices intended for intensive competitive use.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 16
---

# Definition

A device with DS > 8.5, UsbConnDur > 15000, DropHtM > 1.5, and GripDur > 1000, designed to withstand the rigors of frequent transport and intensive use during tournament environments.

# Columns used

* [physicaldurability](/tables/physicaldurability.md): `gripdur`, `drophtm`, `usbconndur`

# Depends on

* [Durability Score (DS)](/knowledge/durability-score.md)
