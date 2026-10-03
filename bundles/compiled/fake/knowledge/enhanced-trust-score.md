---
type: Calculation
title: Enhanced Trust Score (ETS)
description: Calculates trust score considering both profile credibility and content authenticity.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 32
---

# Definition

ETS = 0.5 \times PCI + 0.5 \times CAS

# Depends on

* [Profile Credibility Index (PCI)](/knowledge/profile-credibility-index.md)
* [Content Authenticity Score (CAS)](/knowledge/content-authenticity-score.md)

# Used by

* [Trusted Content Creator](/knowledge/trusted-content-creator.md)
