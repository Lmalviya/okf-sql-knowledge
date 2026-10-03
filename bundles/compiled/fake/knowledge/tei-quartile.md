---
type: Calculation
title: TEI quartile
description: Categorizes accounts into four groups based on their TEI values.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 70
---

# Definition

Q_{TEI} = egin{cases} 1 & 	ext{if TEI} in [0, P_{25}] \ 2 & 	ext{if TEI} in (P_{25}, P_{50}] \ 3 & 	ext{if TEI} in (P_{50}, P_{75}] \ 4 & 	ext{if TEI} in (P_{75}, P_{100}] \end{cases} where P_n represents the nth percentile of TEI values

# Depends on

* [Technical Evasion Index (TEI)](/knowledge/technical-evasion-index.md)

# Used by

* [TEI Risk Category](/knowledge/tei-risk-category.md)
