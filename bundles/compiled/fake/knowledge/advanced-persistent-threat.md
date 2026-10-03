---
type: Business Rule
title: Advanced Persistent Threat
description: Identifies sophisticated, persistent security threats.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 49
---

# Definition

A High-Risk Bot Network with NMI > 0.9 and TEI > 0.8

# Depends on

* [High-Risk Bot Network](/knowledge/high-risk-bot-network.md)
* [Network Manipulation Index (NMI)](/knowledge/network-manipulation-index.md)
* [Technical Evasion Index (TEI)](/knowledge/technical-evasion-index.md)
