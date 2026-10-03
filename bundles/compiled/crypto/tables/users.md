---
type: PostgreSQL Table
title: users
description: '2 columns: userstamp, acctscope.'
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_schema.txt
  title: crypto schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_column_meaning_base.json
  title: crypto column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `userstamp` | character | A CHAR(36) UUID linking to external/client user references (e.g., 'e3bd1f12-3e93-4b3c-a9f3-84be2593a6d7'). |
| `acctscope` | USER-DEFINED | An enum (AcctScope_enum) indicating the account scope (Margin, Spot, Options, Futures). |
