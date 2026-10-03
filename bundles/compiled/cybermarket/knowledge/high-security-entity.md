---
type: Business Rule
title: High-Security Entity
description: Identifies entities with strong security practices
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 24
---

# Definition

An entity with SPS > 80, using military-grade encryption, implementing 2FA or multi-factor authentication, and maintaining fewer than 5 vulnerabilities (vulntally < 5). These entities represent lower security breach risks but may indicate sophisticated operators requiring specialized investigation approaches.

# Columns used

* [securitymonitoring](/tables/securitymonitoring.md): `vulntally`

# Depends on

* [Security Posture Score (SPS)](/knowledge/security-posture-score.md)
