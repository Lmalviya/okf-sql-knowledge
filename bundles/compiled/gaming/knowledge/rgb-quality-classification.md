---
type: Business Rule
title: RGB Quality Classification
description: A systematic framework for categorizing the quality of RGB lighting implementations in gaming peripherals based on the RGB Implementation Quality (RIQ) score.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 51
---

# Definition

A classification system that segments gaming devices into four RGB quality categories: 'Premium RGB Implementation' (RIQ > 8.0) indicating exceptional color accuracy and customization capabilities, 'High-Quality RGB' (RIQ between 6.0 and 8.0) for advanced lighting effects with good color reproduction, 'Standard RGB' (RIQ between 3.0 and 5.9) suitable for basic customization needs, and 'Basic RGB' (RIQ < 3.0) offering limited lighting features, providing standardized comparison metrics for RGB lighting quality across gaming peripherals.

# Depends on

* [RGB Implementation Quality (RIQ)](/knowledge/rgb-implementation-quality.md)
