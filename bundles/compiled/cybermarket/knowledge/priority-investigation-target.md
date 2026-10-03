---
type: Business Rule
title: Priority Investigation Target
description: Identifies cases requiring immediate investigative attention
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 25
---

# Definition

An investigation with IPS > 200, high law enforcement interest (lawinterest = 'High'), involving a suspicious transaction pattern, and connected to a high-risk market. These cases represent the highest priority for resource allocation and immediate intervention.

# Columns used

* [investigation](/tables/investigation.md): `lawinterest`

# Depends on

* [Investigation Priority Score (IPS)](/knowledge/investigation-priority-score.md)
* [High-Risk Market](/knowledge/high-risk-market.md)
* [Suspicious Transaction Pattern](/knowledge/suspicious-transaction-pattern.md)
