---
type: PostgreSQL Table
title: coordinationandevaluation
description: '29 columns: secincidentcount, safetyranking, accesslimitation, coordeffectlvl, partnerorgs, infosharingstate, reportcompliance, dataqualityvalue, monitoringfreq, evaluationstage, lessonslearnedstage, contingencyplanstage, riskmitigationsteps, insurancescope, compliancestate, auditstate, qualitycontrolsteps, stakeholdersatisf, mediacoversentiment, publicperception, documentationstate, lessonsrecorded, bestpracticeslisted, improvementrecs, nextreviewdate, notes. Joins to disasterevents, operations.'
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_schema.txt
  title: disaster schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_column_meaning_base.json
  title: disaster column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `coordevalregistry` | character varying, primary key | A VARCHAR(20) primary key for coordination and evaluation records (e.g., 'COORD0001'). |
| `coorddistref` | character varying | A VARCHAR(20) referencing DisasterEvents(DistRegistry) (e.g., 'DIST0001'). |
| `coordopsref` | character varying | A VARCHAR(20) referencing Operations(OpsRegistry) (e.g., 'OPS0001'). |
| `secincidentcount` | integer | An INT logging how many security incidents have occurred (e.g., 2). |
| `safetyranking` | USER-DEFINED | An enum (SafetyRanking_enum) describing safety level; values: 'Safe', 'Moderate', 'High Risk'. |
| `accesslimitation` | USER-DEFINED | An enum (AccessLimitation_enum) capturing access restrictions; values: 'Severe', 'Partial'. |
| `coordeffectlvl` | USER-DEFINED | An enum (CoordEffectLvl_enum) indicating coordination effectiveness; values: 'Medium', 'Low', 'High'. |
| `partnerorgs` | text | A TEXT field listing partner organizations or supporting groups (e.g., 'NGO-A; LocalGov; RedCross'). |
| `infosharingstate` | USER-DEFINED | An enum (InfoSharingState_enum) for information sharing; values: 'Poor', 'Limited', 'Effective'. |
| `reportcompliance` | numeric | A NUMERIC(4,1) measuring compliance with reporting (e.g., 9.0). |
| `dataqualityvalue` | integer | An INT rating data quality (e.g., 85). |
| `monitoringfreq` | USER-DEFINED | An enum (MonitoringFreq_enum) capturing monitoring frequency; values: 'Monthly', 'Daily', 'Weekly'. |
| `evaluationstage` | USER-DEFINED | An enum (EvaluationStage_enum) describing current evaluation status; values: 'Overdue', 'Due', 'Current'. |
| `lessonslearnedstage` | USER-DEFINED | An enum (LessonsLearnedStage_enum) for how lessons learned documentation is handled; values: 'In Progress', 'Documented', 'Pending'. |
| `contingencyplanstage` | USER-DEFINED | An enum (ContingencyPlanStage_enum) for contingency plan status; values: 'Overdue', 'Due', 'Updated'. |
| `riskmitigationsteps` | USER-DEFINED | An enum (RiskMitigationSteps_enum) describing risk mitigation actions; values: 'Insufficient', 'Partial', 'Adequate'. |
| `insurancescope` | USER-DEFINED | An enum (InsuranceScope_enum) labeling insurance coverage; values: 'Full', 'Partial'. |
| `compliancestate` | USER-DEFINED | An enum (ComplianceState_enum) capturing compliance level; values: 'Partial', 'Compliant', 'Non-Compliant'. |
| `auditstate` | USER-DEFINED | An enum (AuditState_enum) indicating audit status; values: 'Completed', 'Due', 'Overdue'. |
| `qualitycontrolsteps` | USER-DEFINED | An enum (QualityControlSteps_enum) explaining quality control measures; values: 'Moderate', 'Strong', 'Weak'. |
| `stakeholdersatisf` | numeric | A NUMERIC(3,2) rating stakeholder satisfaction (e.g., 8.75). |
| `mediacoversentiment` | USER-DEFINED | An enum (MediaCoverSentiment_enum) denoting media coverage tone; values: 'Positive', 'Neutral', 'Negative'. |
| `publicperception` | numeric | A DECIMAL(5,1) capturing public perception measure (e.g., 75.2). |
| `documentationstate` | USER-DEFINED | An enum (DocumentationState_enum) labeling completeness of documentation; values: 'Partial', 'Incomplete', 'Complete'. |
| `lessonsrecorded` | text | A TEXT field noting documented lessons (e.g., 'More pre-disaster drills needed.'). |
| `bestpracticeslisted` | text | A TEXT field capturing recognized best practices (e.g., 'Daily stand-up meetings, decentralized supply hubs.'). |
| `improvementrecs` | text | A TEXT field logging improvement recommendations (e.g., 'Upgrade transport routes, increase staff training.'). |
| `nextreviewdate` | date | A DATE indicating when the next review is scheduled (e.g., '2026-01-15'). |
| `notes` | text | A TEXT field for extra commentary or insights from coordinators, unbounded length. |

# Joins

* `coorddistref` references `distregistry` in [disasterevents](/tables/disasterevents.md).
* `coordopsref` references `opsregistry` in [operations](/tables/operations.md).

# Related knowledge

* [coordeffectlvl](/knowledge/coordeffectlvl.md)
* [Communication Security Risk (CSR)](/knowledge/communication-security-risk.md)
* [Market Stability Index (MSI)](/knowledge/market-stability-index.md)
* [High-Risk Response Operation](/knowledge/high-risk-response-operation.md)
* [Vulnerable Population Hotspot](/knowledge/vulnerable-population-hotspot.md)
* [Community Engagement Effectiveness (CEE)](/knowledge/community-engagement-effectiveness.md)
* [Cross-Agency Coordination Index (CACI)](/knowledge/cross-agency-coordination-index.md)
* [High-Impact Communication Failure](/knowledge/high-impact-communication-failure.md)
* [Cross-Agency Coordination Crisis](/knowledge/cross-agency-coordination-crisis.md)
