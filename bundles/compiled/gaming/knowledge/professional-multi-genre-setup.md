---
type: Business Rule
title: Professional Multi-Genre Setup
description: Identifies device configurations specifically optimized for players who compete across multiple game genres at a high level.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 42
---

# Definition

A device or device set with GVS > 8.5, ProfCount ≥ 4, and CGPI > 7.5, providing the adaptability and precision required by players who compete across FPS, MOBA, RTS, and other competitive genres.

# Columns used

* [deviceidentity](/tables/deviceidentity.md): `profcount`

# Depends on

* [Gaming Versatility Score (GVS)](/knowledge/gaming-versatility-score.md)
* [Competitive Gaming Performance Index (CGPI)](/knowledge/competitive-gaming-performance-index.md)
