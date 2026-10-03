---
type: Business Rule
title: Effective Leverage Risk Classification
description: Categorizes positions based on their effective leverage to determine risk exposure.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 52
---

# Definition

A position is labeled as 'High Risk' if its Effective Leverage exceeds 20, otherwise as 'Normal'.

# Depends on

* [Effective Leverage](/knowledge/effective-leverage.md)
