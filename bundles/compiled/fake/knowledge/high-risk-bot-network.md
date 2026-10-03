---
type: Business Rule
title: High-Risk Bot Network
description: Identifies dangerous coordinated bot networks.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 40
---

# Definition

A Bot Network with CBR > 0.8 and SRS > 0.7

# Depends on

* [Coordinated Bot Risk (CBR)](/knowledge/coordinated-bot-risk.md)
* [Security Risk Score (SRS)](/knowledge/security-risk-score.md)

# Used by

* [Advanced Persistent Threat](/knowledge/advanced-persistent-threat.md)
