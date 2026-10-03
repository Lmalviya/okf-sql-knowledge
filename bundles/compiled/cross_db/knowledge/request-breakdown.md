---
type: Business Rule
title: Request Breakdown
description: Describes the types and counts of data subject requests.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 71
---

# Definition

An array of strings listing request types and their counts: 'Access: AccReqNum', 'Deletion: DelReqNum', 'Rectification: RectReqNum', 'Portability: PortReqNum', unnested for display

# Columns used

* [auditandcompliance](/tables/auditandcompliance.md): `accreqnum`, `delreqnum`, `rectreqnum`, `portreqnum`
