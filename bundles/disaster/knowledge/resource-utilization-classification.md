---
type: Business Rule
title: Resource Utilization Classification
description: Categorizes distribution hubs based on their Resource Utilization Ratio (RUR) values.
tags: [disaster, logistics]
generated: { by: human:your-name, at: 2026-10-02T17:00:00+05:30 }
sources:
  - id: kb
    resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
    title: disaster business rules (LiveSQLBench), rule 50
---

# Definition

| Class | Condition | Meaning |
|---|---|---|
| High Utilization | RUR > 5 | Possibly overloaded; may need more resources. |
| Moderate Utilization | 2 ≤ RUR ≤ 5 | Balanced use of resources. |
| Low Utilization | RUR < 2 | Underused; resources could be moved elsewhere. |

# Depends on

* [Resource Utilization Ratio (RUR)](/knowledge/resource-utilization-ratio.md), which must be computed first.