---
type: Value Illustration
title: cybermarket|transactions|txstatus
description: Explains the transaction lifecycle stages and their implications
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 3
---

# Definition

'Pending' represents initiated but incomplete transactions awaiting verification or escrow conditions; 'Completed' indicates successfully executed transactions with all parties satisfied; 'Cancelled' denotes transactions terminated before completion, often requiring refund processing; 'Disputed' represents contested transactions requiring arbitration, indicating potential fraud or service failure.

# Columns used

* [transactions](/tables/transactions.md): `txstatus`
