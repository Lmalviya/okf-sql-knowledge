---
type: Calculation
title: Authentication Risk Score (ARS)
description: Assesses authentication-related risks.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 38
---

# Definition

ARS = 0.5 \times TEI + 0.3 \times (1 - PCI) + 0.2 \times SRS

# Depends on

* [Technical Evasion Index (TEI)](/knowledge/technical-evasion-index.md)
* [Profile Credibility Index (PCI)](/knowledge/profile-credibility-index.md)
* [Security Risk Score (SRS)](/knowledge/security-risk-score.md)

# Used by

* [Authentication Risk Account](/knowledge/authentication-risk-account.md)
