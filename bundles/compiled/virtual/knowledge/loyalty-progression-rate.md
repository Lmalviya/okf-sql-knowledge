---
type: Calculation
title: Loyalty Progression Rate (LPR)
description: Measures how quickly a fan is accumulating loyalty within the system
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 15
---

# Definition

LPR = \left(\frac{loypts}{membdays}\right) \times (1 + (engrate \times 2)), \text{ showing points earned per day adjusted by engagement level to identify rapidly advancing fans.}

# Columns used

* [membershipandspending](/tables/membershipandspending.md): `membdays`
* [engagement](/tables/engagement.md): `engrate`

# Used by

* [Rapidly Ascending Fan](/knowledge/rapidly-ascending-fan.md)
