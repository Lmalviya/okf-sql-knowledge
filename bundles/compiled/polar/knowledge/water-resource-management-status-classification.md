---
type: Business Rule
title: Water Resource Management Status Classification (WRMSC)
description: A comprehensive classification system that categorizes water resource management status based on WRMI values to guide operational decisions.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 53
---

# Definition

Water management operations are classified into three status levels: 'Conservation Needed' WHEN (WRMI < 0.5), indicating critical resource limitations requiring immediate conservation measures; 'Monitoring Advised' WHEN (WRMI >= 0.5 AND WRMI < 0.7), representing adequate but vigilant management requiring regular system monitoring; 'Sustainable Management' WHEN (WRMI >= 0.7), indicating optimal water resource utilization suitable for unrestricted operations.

# Depends on

* [Water Resource Management Index (WRMI)](/knowledge/water-resource-management-index.md)
* [Water Conservation Requirement](/knowledge/water-conservation-requirement.md)
