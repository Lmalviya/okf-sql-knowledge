---
type: Business Rule
title: Confirmed Manipulator Under Scrutiny
description: Identifies traders with confirmed manipulative patterns whose cases are under high scrutiny.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 42
---

# Definition

A trader exhibiting a confirmed Market Manipulation Pattern: Layering/Spoofing  AND whose case status is Elevated Regulatory Scrutiny .

# Depends on

* [Market Manipulation Pattern: Layering/Spoofing](/knowledge/market-manipulation-pattern-layering-spoofing.md)
* [Elevated Regulatory Scrutiny](/knowledge/elevated-regulatory-scrutiny.md)
