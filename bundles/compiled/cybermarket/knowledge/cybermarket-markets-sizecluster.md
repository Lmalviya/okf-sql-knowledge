---
type: Value Illustration
title: cybermarket|markets|sizecluster
description: Illustrates the significance of market size classification
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 1
---

# Definition

Size clusters represent market scale and reach: 'Small' markets typically have under 10,000 monthly users and limited vendor presence; 'Medium' markets host 10,000-50,000 monthly users with moderate vendor diversity; 'Large' markets serve 50,000-100,000 users with extensive product catalogs; 'Mega' markets exceed 100,000 monthly users with comprehensive vendor networks and represent the highest-risk monitoring targets.

# Columns used

* [markets](/tables/markets.md): `sizecluster`

# Used by

* [Vendor Network Centrality (VNC)](/knowledge/vendor-network-centrality.md)
