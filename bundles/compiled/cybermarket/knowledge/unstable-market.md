---
type: Business Rule
title: Unstable Market
description: Identifies markets at high risk of imminent shutdown or disruption
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 40
---

# Definition

A market with MVI > 75, MSI < 40, and at least one 'Critical' security alert (alertsev = 'Critical'). These markets typically show signs of administrative instability, declining transaction volumes, and may suggest potential exit scam preparation or law enforcement attention.

# Columns used

* [securitymonitoring](/tables/securitymonitoring.md): `alertsev`

# Depends on

* [cybermarket|securitymonitoring|alertsev](/knowledge/cybermarket-securitymonitoring-alertsev.md)
* [Market Stability Index (MSI)](/knowledge/market-stability-index.md)
* [Market Vulnerability Index (MVI)](/knowledge/market-vulnerability-index.md)
