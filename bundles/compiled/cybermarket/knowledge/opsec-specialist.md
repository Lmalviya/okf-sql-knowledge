---
type: Business Rule
title: OpSec Specialist
description: Identifies entities employing exceptionally sophisticated operational security
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 46
---

# Definition

An entity with OSI > 85, demonstrating Sophisticated Operational Security characteristics, with exceptionally high APL scores (APL > 120), and using either 'Enhanced' or 'Custom' encryption methods (encryptmethod IN ('Enhanced', 'Custom')). These entities represent high-value intelligence targets requiring specialized investigation techniques.

# Columns used

* [communication](/tables/communication.md): `encryptmethod`

# Depends on

* [Anonymity Protection Level (APL)](/knowledge/anonymity-protection-level.md)
* [Sophisticated Operational Security](/knowledge/sophisticated-operational-security.md)
* [Operational Security Index (OSI)](/knowledge/operational-security-index.md)
