---
type: Business Rule
title: Collusion Network Indicator
description: Suggests potential collusion based on investigation details.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 13
---

# Definition

A case indicates potential collusion if `tcirclesz` > 5 AND `grpbehsc` > 0.6 AND `commpat` is 'Regular'.

# Columns used

* [investigationdetails](/tables/investigationdetails.md): `commpat`, `tcirclesz`, `grpbehsc`

# Depends on

* [Suspicion-Weighted Turnover (SWT)](/knowledge/suspicion-weighted-turnover.md)

# Used by

* [High-Risk Collusion Group Member](/knowledge/high-risk-collusion-group-member.md)
* [Networked Mimicry Risk](/knowledge/networked-mimicry-risk.md)
