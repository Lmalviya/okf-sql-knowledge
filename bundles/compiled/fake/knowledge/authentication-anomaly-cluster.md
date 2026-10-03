---
type: Business Rule
title: Authentication Anomaly Cluster
description: Identifies groups with suspicious authentication patterns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 63
---

# Definition

A cluster where average APS < 0.3 and contains at least one Authentication Risk Account

# Depends on

* [Authentication Pattern Score (APS)](/knowledge/authentication-pattern-score.md)
* [Authentication Risk Account](/knowledge/authentication-risk-account.md)
