---
type: Calculation
title: Arbitrage Opportunity Score (AOS)
description: Quantifies the potential arbitrage opportunity considering multiple factors.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 3
---

# Definition

AOS = arbpotential + xexchband + (fundgap \times 2) + basisgap, \text{where these components represent different types of arbitrage opportunities.}

# Used by

* [Arbitrage Window](/knowledge/arbitrage-window.md)
* [Arbitrage ROI](/knowledge/arbitrage-roi.md)
