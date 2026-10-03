---
type: Value Illustration
title: ExhibitionHalls.CCTVCoverage
description: Illustrates CCTV coverage classifications.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 25
---

# Definition

'Full' indicates 100% exhibition space coverage with overlapping cameras, 'Partial' indicates 60-90% coverage with possible blind spots, and 'Limited' indicates less than 60% coverage focusing only on high-value areas.

# Columns used

* [exhibitionhalls](/tables/exhibitionhalls.md): `cctvcoverage`
