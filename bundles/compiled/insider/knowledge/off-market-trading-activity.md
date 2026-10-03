---
type: Value Illustration
title: Off-Market Trading Activity
description: Illustrates types of trading activity occurring outside public exchanges.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 22
---

# Definition

`offmkt`: Describes trades not executed on lit exchanges. 'Internal crosses' specifically refer to a broker matching buy and sell orders from their own clients internally, without routing them to a public exchange. This can be efficient but requires monitoring to ensure fairness and prevent potential conflicts of interest.

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `offmkt`
