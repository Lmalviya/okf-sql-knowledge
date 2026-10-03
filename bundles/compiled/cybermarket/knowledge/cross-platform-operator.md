---
type: Business Rule
title: Cross-Platform Operator
description: Identifies entities operating across multiple cybermarket platforms
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 29
---

# Definition

An entity identified through matching cryptographic or communication fingerprints (keymatchcount > 30) operating on three or more markets simultaneously, maintaining consistent security practices, and exhibiting similar transaction patterns across platforms. These operators represent higher-value intelligence targets due to their broader cybermarket ecosystem involvement.

# Columns used

* [communication](/tables/communication.md): `keymatchcount`

# Used by

* [Multi-Platform Threat Entity](/knowledge/multi-platform-threat-entity.md)
