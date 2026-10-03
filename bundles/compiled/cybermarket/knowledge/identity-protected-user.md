---
type: Business Rule
title: Identity-Protected User
description: Identifies users with robust anonymity protections
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 26
---

# Definition

A user with APL > 100, consistently using TOR (tornodecount > 20), employing VPN protection (vpnflag = 'Yes'), and utilizing custom encryption methods. These users demonstrate sophisticated operational security requiring specialized investigation techniques.

# Columns used

* [communication](/tables/communication.md): `tornodecount`, `vpnflag`

# Depends on

* [Anonymity Protection Level (APL)](/knowledge/anonymity-protection-level.md)
