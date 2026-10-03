---
type: Value Illustration
title: Dark Pool Usage Venues
description: Explains the nature of dark pool usage indicated in transaction records.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 21
---

# Definition

`darkusage`: This field lists Alternative Trading Systems (ATS) or other dark pools used. 'ATS-X', 'ATS-Y' are anonymized identifiers for specific dark pools, which are private exchanges where large orders can be executed without revealing intent to the public market, potentially reducing market impact. Usage patterns can be analyzed for regulatory compliance (e.g., ensuring best execution) or signs of avoiding market transparency.

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `darkusage`

# Used by

* [Potentially Evasive Order Modifier](/knowledge/potentially-evasive-order-modifier.md)
