---
type: PostgreSQL Table
title: researchprocess
description: '11 columns: analysisprio, followstat, peerrevstat, pubstat, resprio, fundstat, collabstat, secclass, discstat, notesmemo. Joins to signals.'
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_schema.txt
  title: alien schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_column_meaning_base.json
  title: alien column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `signalref` | character, primary key | Full name: 'Signal Registry Reference'. Explanation: Foreign key referencing the main signal record. Data type: CHAR(36). Example: 'SIG-MNO-7890'. |
| `analysisprio` | text | Full name: 'Analysis Priority'. Explanation: Priority assigned for analyzing this signal. Data type: TEXT. Possible categories: High, Low, Medium, Urgent. |
| `followstat` | character varying | Full name: 'Follow-up Status'. Explanation: Status of any follow-up observations. Data type: VARCHAR(25). Possible categories: Completed, Required, Scheduled. |
| `peerrevstat` | character varying | Full name: 'Peer Review Status'. Explanation: Where this signal stands in peer review. Data type: VARCHAR(25). Possible categories: Completed, In Progress, Pending. |
| `pubstat` | character | Full name: 'Publication Status'. Explanation: Whether findings about the signal have been published. Data type: CHAR(25). Possible categories: Draft, Published, Submitted. |
| `resprio` | character varying | Full name: 'Research Priority'. Explanation: How urgently this signal needs scientific attention. Data type: VARCHAR(30). Possible categories: High, Low, Medium. |
| `fundstat` | character | Full name: 'Funding Status'. Explanation: Funding situation for further study. Data type: VARCHAR(30). Possible categories: Funded, Pending, Unfunded. |
| `collabstat` | character | Full name: 'Collaboration Status'. Explanation: The nature of collaboration on this signal. Data type: VARCHAR(35). Possible categories: International, Solo, Team. |
| `secclass` | character | Full name: 'Security Classification'. Explanation: Visibility and clearance level for the data. Data type: CHAR(35). Possible categories: Classified, Public, Restricted. |
| `discstat` | character varying | Full name: 'Disclosure Status'. Explanation: How much information about the signal is shared publicly. Data type: VARCHAR(40). Possible categories: Full, None, Partial. |
| `notesmemo` | text | Full name: 'Research Notes'. Explanation: Any extra remarks or context by researchers. Data type: TEXT. Example: 'Project requires further funding...' |

# Joins

* `signalref` references `signalregistry` in [signals](/tables/signals.md).
