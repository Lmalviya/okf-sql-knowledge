---
type: Calculation
title: Credit Risk Intensity (CRI)
description: Advanced measure of credit risk that incorporates payment history and account diversity.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 36
---

# Definition

CRI = 0.5 × (1 - \frac{credscore}{850}) + 0.3 × \frac{delinqcount + latepaycount + choffs}{10} + 0.2 × (1 - AHI), \text{where AHI is the Account Health Index}

# Columns used

* [credit_and_compliance](/tables/credit_and_compliance.md): `credscore`, `delinqcount`, `latepaycount`, `choffs`

# Depends on

* [Account Health Index (AHI)](/knowledge/account-health-index.md)

# Used by

* [Declining Credit Health](/knowledge/declining-credit-health.md)
