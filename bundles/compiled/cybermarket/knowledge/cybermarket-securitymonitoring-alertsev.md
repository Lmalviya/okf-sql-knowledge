---
type: Value Illustration
title: cybermarket|securitymonitoring|alertsev
description: Explains the alert severity classification system
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 9
---

# Definition

'Low' alerts indicate minor anomalies requiring minimal attention and posing limited security risk; 'Medium' alerts signal notable deviations from baseline behavior requiring investigation within standard timeframes; 'High' alerts denote significant security concerns demanding prompt attention and intervention; 'Critical' alerts represent severe and immediate security threats requiring urgent action and potential emergency response protocols.

# Columns used

* [securitymonitoring](/tables/securitymonitoring.md): `alertsev`

# Used by

* [Market Vulnerability Index (MVI)](/knowledge/market-vulnerability-index.md)
* [Unstable Market](/knowledge/unstable-market.md)
