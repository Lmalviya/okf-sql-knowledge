---
type: Value Illustration
title: Enhanced Churn Risk Severity Classification
description: Defines detailed categorization for high-risk churn candidates requiring intervention
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 54
---

# Definition

Enhances the standard churn risk classification by adding a 'Severe' category for critically at-risk users. The classification uses precise RRF thresholds: 'Severe' identifies users with RRF > 4.5 requiring immediate intervention and executive attention; 'High' identifies users with RRF between 3.5-4.5 requiring prioritized retention campaigns; 'Medium' applies to users with RRF between 2.5-3.5 requiring standard monitoring. This refined classification enables more targeted allocation of retention resources based on urgency level and churn probability.

# Depends on

* [Retention Risk Factor (RRF)](/knowledge/retention-risk-factor.md)
