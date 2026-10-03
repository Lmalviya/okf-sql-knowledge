---
type: Business Rule
title: Artifact Rarity & Valuation (ARV)
description: Establishes criteria for identifying artifacts of exceptional rarity and valuation that demand heightened preservation measures and limited public access.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 55
---

# Definition

Artifacts are categorized as ARV if their insurance value exceed $1,000,000.
