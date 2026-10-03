---
type: Business Rule
title: High-Risk Collusion Group Member
description: Identifies traders within a suspected collusion network who individually exhibit high-risk behavior.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 43
---

# Definition

A trader flagged by the Collusion Network Indicator  AND who also meets the High-Risk Trader Profile  criteria.

# Depends on

* [High-Risk Trader Profile](/knowledge/high-risk-trader-profile.md)
* [Collusion Network Indicator](/knowledge/collusion-network-indicator.md)
