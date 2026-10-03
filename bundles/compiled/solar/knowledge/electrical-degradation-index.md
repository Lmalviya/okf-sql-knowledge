---
type: Calculation
title: Electrical Degradation Index (EDI)
description: Measures the combined degradation of electrical parameters.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 38
---

# Definition

EDI = (FillFactorInitial - FillFactorCurrent)/FillFactorInitial + (VocInitialV - VocCurrV)/VocInitialV + (IscInitialA - IscCurrA)/IscInitialA, where higher values indicate more severe degradation.

# Columns used

* [electrical](/tables/electrical.md): `isccurra`, `voccurrv`

# Depends on

* [FillFactor (Fill Factor)](/knowledge/fillfactor.md)
