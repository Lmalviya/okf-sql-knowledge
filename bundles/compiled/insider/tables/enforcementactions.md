---
type: PostgreSQL Table
title: enforcementactions
description: '23 columns: acttake, esclvl, resstat, penimp, penamt, legactstat, settlestat, repimp, busrestr, remedstat, traderestr, sysupdneed, polupdneed, trainreq, repgenstat, dataretstat, auditstat, conflvl, accrestr, datashare. Joins to compliancecase, investigationdetails.'
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_schema.txt
  title: insider schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_column_meaning_base.json
  title: insider column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `enforcereg` | character varying, primary key | VARCHAR(50). Primary key for an enforcement‑action record. |
| `compref2` | character varying | VARCHAR(50). Foreign‑key to ComplianceCase.CompReg against which action is taken. |
| `acttake` | USER-DEFINED | action_taken_enum (enum: 'Warning', 'Restriction', 'Suspension'). Enforcement action applied. |
| `esclvl` | USER-DEFINED | escalation_level_enum (enum: 'Supervisor', 'Compliance', 'Legal'). Escalation destination within the organisation. |
| `resstat` | USER-DEFINED | resolution_status_enum (enum: 'Pending', 'In Progress', 'Resolved'). Resolution progress status. |
| `penimp` | USER-DEFINED | penalty_imposed_enum (enum: 'Warning', 'Fine', 'Ban'). Type of penalty imposed, if any. |
| `penamt` | numeric | NUMERIC(20,2). Monetary amount of fines or restitution in USD (e.g., 150 000.00). |
| `legactstat` | USER-DEFINED | legal_action_status_enum (enum: 'Pending', 'Active'). Status of any legal proceedings. |
| `settlestat` | USER-DEFINED | settlement_status_enum (enum: 'Negotiating', 'Settled'). Settlement progress with regulators or plaintiffs. |
| `repimp` | USER-DEFINED | reputation_impact_enum (enum: 'Minimal', 'Moderate', 'Severe'). Estimated reputational impact. |
| `busrestr` | USER-DEFINED | business_restriction_enum (enum: 'Partial', 'Full'). Extent of business restrictions imposed. |
| `remedstat` | USER-DEFINED | remediation_status_enum (enum: 'Not Required', 'Pending', 'Completed'). Status of required remediation actions. |
| `traderestr` | USER-DEFINED | trading_restriction_period_enum (enum: 'Blackout', 'Special'). Type of imposed trading restriction period. |
| `sysupdneed` | USER-DEFINED | system_update_needed_enum (enum: 'No', 'Minor', 'Major'). Whether surveillance systems require updates. |
| `polupdneed` | USER-DEFINED | policy_update_needed_enum (enum: 'No', 'Yes', 'Urgent'). Need for policy updates. |
| `trainreq` | USER-DEFINED | training_requirement_enum (enum: 'Refresher', 'Comprehensive'). Mandatory training requirement type. |
| `repgenstat` | USER-DEFINED | report_generation_status_enum (enum: 'Manual', 'Automated', 'Hybrid'). How enforcement reports are generated. |
| `dataretstat` | USER-DEFINED | data_retention_status_enum (enum: 'Current', 'Archived', 'Deleted'). Data‑retention status for case records. |
| `auditstat` | USER-DEFINED | audit_trail_status_enum (enum: 'Complete', 'Partial', 'Missing'). Audit‑trail completeness for the action. |
| `conflvl` | USER-DEFINED | confidentiality_level_enum (enum: 'Normal', 'Sensitive', 'Highly Sensitive'). Confidentiality level of the case data. |
| `accrestr` | USER-DEFINED | access_restriction_enum (enum: 'Public', 'Internal', 'Restricted'). Access restrictions applied to the case. |
| `datashare` | USER-DEFINED | data_sharing_status_enum (enum: 'Allowed', 'Limited', 'Prohibited'). Data‑sharing status with external parties. |
| `invdetref` | character varying | VARCHAR(50). Optional foreign‑key to InvestigationDetails.InvDetReg providing underlying investigation context. |

# Joins

* `compref2` references `compreg` in [compliancecase](/tables/compliancecase.md).
* `invdetref` references `invdetreg` in [investigationdetails](/tables/investigationdetails.md).

# Related knowledge

* [Enforcement Financial Impact Ratio (EFIR)](/knowledge/enforcement-financial-impact-ratio.md)
* [Significant Enforcement Action](/knowledge/significant-enforcement-action.md)
* [Trading Restriction Period Types](/knowledge/trading-restriction-period-types.md)
* [Logarithmic Enforcement Fine Impact (LEFI)](/knowledge/logarithmic-enforcement-fine-impact.md)
* [Premature Resolution Block](/knowledge/premature-resolution-block.md)
