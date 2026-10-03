---
type: Business Rule
title: High-Risk Manipulator Candidate
description: Identifies traders flagged for both high-risk profiles and specific market manipulation patterns.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 60
---

# Definition

A trader who meets the High-Risk Trader Profile  AND is flagged for Market Manipulation Pattern: Layering/Spoofing .

# Depends on

* [High-Risk Trader Profile](/knowledge/high-risk-trader-profile.md)
* [Market Manipulation Pattern: Layering/Spoofing](/knowledge/market-manipulation-pattern-layering-spoofing.md)
