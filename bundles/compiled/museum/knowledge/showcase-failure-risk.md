---
type: Business Rule
title: Showcase Failure Risk
description: Identifies showcases at risk of failing to maintain proper environmental conditions.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 16
---

# Definition

Occurs when SESR < 4 OR at least three of the following are true: SealCondition='Poor', MaintStatus='Overdue', FilterStatus='Replace Now', SilicaGelStatus='Replace Now'.

# Columns used

* [showcases](/tables/showcases.md): `sealcondition`, `maintstatus`, `filterstatus`, `silicagelstatus`

# Depends on

* [Showcase Environmental Stability Rating (SESR)](/knowledge/showcase-environmental-stability-rating.md)
