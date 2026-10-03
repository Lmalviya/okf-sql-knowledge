---
type: Business Rule
title: Compromised Shipment
description: Identifies shipments with serious integrity issues.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 11
---

# Definition

A shipment with IntegrityMark='Compromised' or SealFlag='Broken' or TamperSign='Confirmed'

# Columns used

* [shipments](/tables/shipments.md): `integritymark`, `sealflag`, `tampersign`
