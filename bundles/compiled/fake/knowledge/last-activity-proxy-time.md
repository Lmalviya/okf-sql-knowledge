---
type: Calculation
title: last activity proxy time
description: An estimated timestamp of the last known activity for an account, used when direct session timestamps are unavailable or insufficient.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 84
---

# Definition

Derived as \max(\text{detecttime}) from associated securitydetection records for an account.

# Columns used

* [securitydetection](/tables/securitydetection.md): `detecttime`

# Used by

* [review priority](/knowledge/review-priority.md)
* [Account Inactivity](/knowledge/account-inactivity.md)
