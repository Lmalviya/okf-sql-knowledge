---
type: Calculation
title: influence ranking by NIC
description: A ranking system that orders accounts based on their NIC scores from highest to lowest.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 78
---

# Definition

\text{rank}_i = |\{j : \text{NIC}_j > \text{NIC}_i\}| + 1 where i is the current account and j iterates over all accounts

# Depends on

* [Network Influence Centrality (NIC)](/knowledge/network-influence-centrality.md)
