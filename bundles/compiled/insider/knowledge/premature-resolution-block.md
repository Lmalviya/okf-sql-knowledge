---
type: Business Rule
title: Premature Resolution Block
description: A business rule preventing an enforcement action from being marked as 'Resolved' if associated risk metrics (like III) exceed a predefined threshold, ensuring high-risk cases receive sufficient review.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 72
---

# Definition

Block UPDATE of enforcementactions.resstat to 'Resolved' IF linked investigationdetails yield an Investigation Intensity Index > 75

# Columns used

* [enforcementactions](/tables/enforcementactions.md): `resstat`

# Depends on

* [Investigation Intensity Index (III)](/knowledge/investigation-intensity-index.md)
