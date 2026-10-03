---
type: Calculation
title: Socio-Environmental Support Index (SESI)
description: Computes a composite index reflecting the quality of the patient's social environment and the facility's resource context.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 35
---

# Definition

SESI = \frac{SSE_{avg} + FRAI}{2}, \text{combining average Social Support Effectiveness (SSE) across patients with Facility Resource Adequacy Index (FRAI)}

# Depends on

* [Social Support Effectiveness (SSE)](/knowledge/social-support-effectiveness.md)
* [Facility Resource Adequacy Index (FRAI)](/knowledge/facility-resource-adequacy-index.md)
