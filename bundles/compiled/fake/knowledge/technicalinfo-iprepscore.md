---
type: Value Illustration
title: technicalinfo.iprepscore
description: Illustrates IP reputation scoring.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 25
---

# Definition

Ranges from 0 to 1. Scores above 0.8 indicate trusted IPs, while scores below 0.3 suggest potentially malicious or compromised IPs.

# Columns used

* [technicalinfo](/tables/technicalinfo.md): `iprepscore`
