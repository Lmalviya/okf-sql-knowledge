---
type: Value Illustration
title: Trading Restriction Period Types
description: Explains the types of trading restrictions imposed as part of enforcement.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 29
---

# Definition

`traderestr`: 'Blackout' typically refers to a complete prohibition on trading specific securities or during certain periods (e.g., around earnings announcements). 'Special' indicates other, specific restrictions tailored to the case, which might include limits on order types, position sizes, or requiring pre-trade approvals.

# Columns used

* [enforcementactions](/tables/enforcementactions.md): `traderestr`
