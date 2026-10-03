---
type: Business Rule
title: Battery Efficiency Classification
description: A categorical framework for evaluating and classifying the battery efficiency of gaming devices based on their Battery Efficiency Ratio (BER).
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 50
---

# Definition

A classification system that segments wireless gaming devices into four efficiency categories: 'Excellent Efficiency' (BER > 7.5) indicating marathon gaming capability, 'Good Efficiency' (BER between 5.0 and 7.5) for extended gaming sessions, 'Average Efficiency' (BER between 2.5 and 4.9) suitable for regular gameplay, and 'Poor Efficiency' (BER < 2.5) requiring frequent recharging, providing standardized comparison metrics across different gaming peripherals.

# Depends on

* [Battery Efficiency Ratio (BER)](/knowledge/battery-efficiency-ratio.md)
