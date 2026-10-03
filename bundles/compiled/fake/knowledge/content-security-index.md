---
type: Calculation
title: Content Security Index (CSI)
description: Evaluates content security considering manipulation and authenticity.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 34
---

# Definition

CSI = 0.7 \times (1 - CMS) + 0.3 \times CAS

# Depends on

* [Content Manipulation Score (CMS)](/knowledge/content-manipulation-score.md)
* [Content Authenticity Score (CAS)](/knowledge/content-authenticity-score.md)
