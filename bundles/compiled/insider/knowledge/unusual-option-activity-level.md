---
type: Value Illustration
title: Unusual Option Activity Level
description: Illustrates the degree of detected unusual options trading volume or types.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 26
---

# Definition

`unuoptact`: 'High' suggests significant deviations from normal option trading patterns in terms of volume, strike prices, or expiration dates, potentially indicating informed trading or speculation ahead of news. 'Moderate' indicates some unusual activity, but less pronounced. This can be a flag for investigating potential insider information.

# Columns used

* [sentimentandfundamentals](/tables/sentimentandfundamentals.md): `unuoptact`
