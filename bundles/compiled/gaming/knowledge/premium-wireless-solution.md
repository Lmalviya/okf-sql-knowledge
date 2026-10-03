---
type: Business Rule
title: Premium Wireless Solution
description: Defines high-end wireless gaming devices with performance comparable to wired alternatives.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 18
---

# Definition

A device with WPR > 9.0, ConnType = 'Wireless 2.4GHz', LatMs < 2.5, and BattLifeH > 24, eliminating common wireless drawbacks while maintaining the convenience of cable-free operation.

# Columns used

* [testsessions](/tables/testsessions.md): `battlifeh`, `latms`
* [deviceidentity](/tables/deviceidentity.md): `conntype`

# Depends on

* [Wireless Performance Rating (WPR)](/knowledge/wireless-performance-rating.md)
