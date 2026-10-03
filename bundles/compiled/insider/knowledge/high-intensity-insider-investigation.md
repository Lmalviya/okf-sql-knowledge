---
type: Business Rule
title: High-Intensity Insider Investigation
description: Flags investigations triggered by potential insider trading that show high intensity scores, suggesting significant findings.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 67
---

# Definition

An investigation linked to a Potential Insider Trading Flag  AND having a high Investigation Intensity Index (III)  (e.g., > 70).

# Depends on

* [Investigation Intensity Index (III)](/knowledge/investigation-intensity-index.md)
* [Potential Insider Trading Flag](/knowledge/potential-insider-trading-flag.md)
