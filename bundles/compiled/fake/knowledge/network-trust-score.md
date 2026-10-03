---
type: Calculation
title: Network Trust Score (NTS)
description: Evaluates trustworthiness of account's network connections.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 36
---

# Definition

NTS = PCI \times (1 - NGV) \times (1 - CBR)

# Depends on

* [Profile Credibility Index (PCI)](/knowledge/profile-credibility-index.md)
* [Network Growth Velocity (NGV)](/knowledge/network-growth-velocity.md)
* [Coordinated Bot Risk (CBR)](/knowledge/coordinated-bot-risk.md)

# Used by

* [Network Security Threat](/knowledge/network-security-threat.md)
