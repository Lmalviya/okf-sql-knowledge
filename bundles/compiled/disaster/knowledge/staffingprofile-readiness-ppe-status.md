---
type: Value Illustration
title: staffingProfile.readiness.ppe_status
description: Illustrates the availability of Personal Protective Equipment
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 8
---

# Definition

Adequate means sufficient PPE available for all personnel, Limited indicates restrictions in PPE distribution requiring prioritization, and Critical represents severe shortages threatening staff safety and operational continuity

# Columns used

* [humanresources](/tables/humanresources.md): `staffingprofile`

# Used by

* [Staffing to Need Ratio (SNR)](/knowledge/staffing-to-need-ratio.md)
* [Critical Health Response Requirement](/knowledge/critical-health-response-requirement.md)
