---
type: Business Rule
title: VPN Abuser
description: Identifies accounts systematically using VPNs.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 16
---

# Definition

An account with TEI > 0.8 and at least 3 different countries in login locations

# Depends on

* [Technical Evasion Index (TEI)](/knowledge/technical-evasion-index.md)

# Used by

* [Authentication Risk Account](/knowledge/authentication-risk-account.md)
