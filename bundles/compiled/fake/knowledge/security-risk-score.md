---
type: Calculation
title: Security Risk Score (SRS)
description: Calculates overall security risk based on multiple factors.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 4
---

# Definition

SRS = 0.4 \times \text{riskval} + 0.3 \times (1 - \text{trustval}) + 0.3 \times \text{impactval}

# Columns used

* [moderationaction](/tables/moderationaction.md): `trustval`, `impactval`

# Used by

* [High-Risk Account](/knowledge/high-risk-account.md)
* [Cross-Platform Risk Index (CPRI)](/knowledge/cross-platform-risk-index.md)
* [Authentication Risk Score (ARS)](/knowledge/authentication-risk-score.md)
* [High-Risk Bot Network](/knowledge/high-risk-bot-network.md)
* [Reputation Volatility Index (RVI)](/knowledge/reputation-volatility-index.md)
