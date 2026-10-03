---
type: Calculation
title: Retention Risk Factor (RRF)
description: Quantifies the risk of fan churn based on multiple behavioral indicators
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 13
---

# Definition

RRF = (1 - intconsist) \times 2 + \left(\frac{CURRENT\_DATE - lastlogdt}{30}\right) \times 0.5 + \left(\frac{churnflag\_numeric}{3}\right) \times 2, \text{ where churnflag\_numeric maps churnflag enum: None=0, Low=1, Medium=2, High=3.}

# Columns used

* [preferencesandsettings](/tables/preferencesandsettings.md): `lastlogdt`, `intconsist`
* [retentionandinfluence](/tables/retentionandinfluence.md): `churnflag`

# Depends on

* [Churn Risk Numeric Mapping](/knowledge/churn-risk-numeric-mapping.md)

# Used by

* [Fan Lifetime Value (FLV)](/knowledge/fan-lifetime-value.md)
* [Churn Candidate](/knowledge/churn-candidate.md)
* [Investment Recovery Period (IRP)](/knowledge/investment-recovery-period.md)
* [Churn Prevention Investment (CPI)](/knowledge/churn-prevention-investment.md)
* [Retention Risk Superfan](/knowledge/retention-risk-superfan.md)
* [Enhanced Churn Risk Severity Classification](/knowledge/enhanced-churn-risk-severity-classification.md)
