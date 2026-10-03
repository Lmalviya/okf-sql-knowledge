---
type: Calculation
title: Total Post Frequency (TPF)
description: Measures the total posting frequency across all sessions for an account.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 76
---

# Definition

TPF_a = \sum_{\text{cntref} \in \text{contentbehavior}} \text{postfreq}, \quad \text{where } \text{cntsessref} = \text{sessref}, \text{sessprofref} = \text{profkey}, \text{profaccref} = a

# Columns used

* [profile](/tables/profile.md): `profkey`, `profaccref`
* [sessionbehavior](/tables/sessionbehavior.md): `sessref`, `sessprofref`
* [contentbehavior](/tables/contentbehavior.md): `cntref`, `cntsessref`, `postfreq`

# Used by

* [High-Activity Account](/knowledge/high-activity-account-77.md)
