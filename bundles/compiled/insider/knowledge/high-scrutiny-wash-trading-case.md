---
type: Business Rule
title: High-Scrutiny Wash Trading Case
description: Identifies compliance cases involving high-volume wash trading concerns that are also under elevated regulatory scrutiny.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 63
---

# Definition

A compliance case flagged for Elevated Regulatory Scrutiny  AND linked to a High-Volume Wash Trading Concern .

# Depends on

* [Elevated Regulatory Scrutiny](/knowledge/elevated-regulatory-scrutiny.md)
* [High-Volume Wash Trading Concern](/knowledge/high-volume-wash-trading-concern.md)
