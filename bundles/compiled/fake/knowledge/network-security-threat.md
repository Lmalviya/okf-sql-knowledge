---
type: Business Rule
title: Network Security Threat
description: Identifies accounts posing network-level security risks.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 43
---

# Definition

An account with NTS < 0.3 and is part of a Bot Network

# Depends on

* [Network Trust Score (NTS)](/knowledge/network-trust-score.md)
* [Bot Network](/knowledge/bot-network.md)
