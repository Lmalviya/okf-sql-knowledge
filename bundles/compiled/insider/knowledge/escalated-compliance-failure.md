---
type: Business Rule
title: Escalated Compliance Failure
description: Identifies traders with a problematic compliance history who have now incurred significant enforcement actions.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 61
---

# Definition

A trader identified with Problematic Compliance History  AND subject to a Significant Enforcement Action .

# Depends on

* [Problematic Compliance History](/knowledge/problematic-compliance-history.md)
* [Significant Enforcement Action](/knowledge/significant-enforcement-action.md)
