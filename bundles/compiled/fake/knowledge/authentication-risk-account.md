---
type: Business Rule
title: Authentication Risk Account
description: Identifies accounts with suspicious authentication patterns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 42
---

# Definition

An account with ARS > 0.7 and at least one VPN Abuser detection

# Depends on

* [Authentication Risk Score (ARS)](/knowledge/authentication-risk-score.md)
* [VPN Abuser](/knowledge/vpn-abuser.md)

# Used by

* [Authentication Anomaly Cluster](/knowledge/authentication-anomaly-cluster.md)
