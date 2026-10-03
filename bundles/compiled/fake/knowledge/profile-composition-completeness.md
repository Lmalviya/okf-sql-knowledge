---
type: Value Illustration
title: profile_composition.completeness
description: Illustrates profile completeness scoring.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 26
---

# Definition

Ranges from 0 to 1. Values above 0.8 indicate well-maintained profiles, while values below 0.4 suggest placeholder or abandoned profiles.

# Columns used

* [profile](/tables/profile.md): `profile_composition`
