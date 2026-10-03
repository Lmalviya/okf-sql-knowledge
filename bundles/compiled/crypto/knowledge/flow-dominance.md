---
type: Business Rule
title: Flow Dominance
description: Categorizes market flow based on which group (smart money, retail, or institutional) has the highest trading volume.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 50
---

# Definition

Categorized as 'Smart Money Dominant' when smartforce > retail_flow * 1.2 AND smartforce > inst_flow * 1.2; 'Retail Dominant' when retail_flow > smartforce * 1.2 AND retail_flow > inst_flow * 1.2; 'Institutional Dominant' when inst_flow > smartforce * 1.2 AND inst_flow > retail_flow * 1.2; otherwise 'Mixed'.
