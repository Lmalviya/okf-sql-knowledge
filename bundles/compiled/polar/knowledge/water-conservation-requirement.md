---
type: Business Rule
title: Water Conservation Requirement
description: Specifies the conditions under which water conservation measures must be implemented.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 18
---

# Definition

Water conservation measures must be implemented when the WRMI falls below 0.5, indicating either low water levels, poor water quality, or high waste tank levels that require immediate attention to maintain sustainable water usage.

# Depends on

* [Water Resource Management Index (WRMI)](/knowledge/water-resource-management-index.md)

# Used by

* [Water Resource Management Status Classification (WRMSC)](/knowledge/water-resource-management-status-classification.md)
