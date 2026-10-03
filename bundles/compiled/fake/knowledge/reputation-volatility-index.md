---
type: Calculation
title: Reputation Volatility Index (RVI)
description: Quantifies stability of account reputation over time.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 53
---

# Definition

RVI = \frac{\sigma_{\text{reputscore}}}{\mu_{\text{reputscore}}} \times (1 + \frac{|\Delta\text{reputscore}|}{\Delta t})

# Columns used

* [moderationaction](/tables/moderationaction.md): `reputscore`

# Depends on

* [Profile Credibility Index (PCI)](/knowledge/profile-credibility-index.md)
* [Security Risk Score (SRS)](/knowledge/security-risk-score.md)

# Used by

* [Behavioral Consistency Score (BCS)](/knowledge/behavioral-consistency-score.md)
* [Reputation Manipulation Ring](/knowledge/reputation-manipulation-ring.md)
