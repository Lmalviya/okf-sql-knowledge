---
type: Business Rule
title: Conservation Priority Level
description: Classifies artifacts into priority levels based on their CPI scores
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 56
---

# Definition

'High Priority': CPI > 7 (Artifacts requiring immediate conservation attention); 'Medium Priority': 4 < CPI ≤ 7 (Artifacts needing monitoring and planned conservation); 'Low Priority': CPI ≤ 4 (Artifacts in stable condition).

# Depends on

* [Conservation Priority Index (CPI)](/knowledge/conservation-priority-index.md)
