---
type: Business Rule
title: Severe Chronic Violator Case
description: Identifies compliance cases under elevated scrutiny involving traders flagged as chronic compliance violators.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 68
---

# Definition

A compliance case flagged for Elevated Regulatory Scrutiny  AND involving a trader identified as a Chronic Compliance Violator .

# Depends on

* [Elevated Regulatory Scrutiny](/knowledge/elevated-regulatory-scrutiny.md)
* [Chronic Compliance Violator](/knowledge/chronic-compliance-violator.md)
