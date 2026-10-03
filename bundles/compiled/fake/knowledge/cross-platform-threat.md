---
type: Business Rule
title: Cross-Platform Threat
description: Identifies threats operating across multiple platforms.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 46
---

# Definition

A High-Risk Account with CPRI > 0.9 and is part of a Sockpuppet Network

# Depends on

* [High-Risk Account](/knowledge/high-risk-account.md)
* [Cross-Platform Risk Index (CPRI)](/knowledge/cross-platform-risk-index.md)
* [Sockpuppet Network](/knowledge/sockpuppet-network.md)

# Used by

* [Multi-Platform Threat Network](/knowledge/multi-platform-threat-network.md)
