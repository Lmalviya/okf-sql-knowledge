---
type: Calculation
title: Automated Behavior Score (ABS)
description: Measures degree of automation in account behavior.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 35
---

# Definition

ABS = 0.4 \times BBI + 0.3 \times TEI + 0.3 \times (1 - CAS)

# Depends on

* [Bot Behavior Index (BBI)](/knowledge/bot-behavior-index.md)
* [Technical Evasion Index (TEI)](/knowledge/technical-evasion-index.md)
* [Content Authenticity Score (CAS)](/knowledge/content-authenticity-score.md)

# Used by

* [Automated Spam Network](/knowledge/automated-spam-network.md)
* [Multi-Account Correlation Index (MACI)](/knowledge/multi-account-correlation-index.md)
