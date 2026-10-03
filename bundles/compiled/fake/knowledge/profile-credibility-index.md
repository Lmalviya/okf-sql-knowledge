---
type: Calculation
title: Profile Credibility Index (PCI)
description: Evaluates overall profile credibility.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 5
---

# Definition

PCI = 0.3 \times \text{credscore} + 0.3 \times \text{reputscore} + 0.4 \times \text{completeness}

# Columns used

* [moderationaction](/tables/moderationaction.md): `credscore`, `reputscore`

# Used by

* [Trusted Account](/knowledge/trusted-account.md)
* [Enhanced Trust Score (ETS)](/knowledge/enhanced-trust-score.md)
* [Network Trust Score (NTS)](/knowledge/network-trust-score.md)
* [Authentication Risk Score (ARS)](/knowledge/authentication-risk-score.md)
* [Reputation Volatility Index (RVI)](/knowledge/reputation-volatility-index.md)
