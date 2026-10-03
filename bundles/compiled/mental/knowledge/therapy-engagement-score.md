---
type: Calculation
title: Therapy Engagement Score (TES)
description: Computes an average engagement score across therapy sessions.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 4
---

# Definition

TES = \frac{\sum_{i \in treatmentbasics} (therapy\_details_i['engagement\_score'])} {|treatmentbasics|}, \text{where } engagement\_score = \begin{cases} 3 & \text{if } therapy\_details['engagement'] = High \\ 2 & \text{if } therapy\_details['engagement'] = Medium \\ 1 & \text{if } therapy\_details['engagement'] = Low \\ 0 & \text{if } therapy\_details['engagement'] = Non-compliant \end{cases}, \text{and } therapy\_details \text{ is the JSONB column in the treatmentbasics table}

# Used by

* [Low Engagement Risk](/knowledge/low-engagement-risk.md)
* [Engagement-Adherence Score (EAS)](/knowledge/engagement-adherence-score.md)
* [Engagement Deficit Index (EDI)](/knowledge/engagement-deficit-index.md)
* [Facility with Potential Treatment Inertia](/knowledge/facility-with-potential-treatment-inertia.md)
* [Therapeutic Alliance & Engagement Score (TAES)](/knowledge/therapeutic-alliance-engagement-score.md)
* [Facility with Potential Engagement-Outcome Disconnect](/knowledge/facility-with-potential-engagement-outcome-disconnect.md)
