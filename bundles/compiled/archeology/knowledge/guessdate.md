---
type: Value Illustration
title: GuessDate (Estimated Dating)
description: Illustrates dating conventions in archaeological classification for chronological placement.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 29
---

# Definition

Values like '3500-3000 BCE', '1st c. CE', or 'ca. 1450 CE' represent estimated chronological placement based on excavation findings. Precision varies from specific years to century-level estimates depending on available evidence and dating methodologies employed.

# Columns used

* [sites](/tables/sites.md): `guessdate`

# Used by

* [Conservation Priority Index (CPI)](/knowledge/conservation-priority-index.md)
* [High Temporal Value Site](/knowledge/high-temporal-value-site.md)
