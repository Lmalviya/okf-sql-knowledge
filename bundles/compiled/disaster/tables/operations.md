---
type: PostgreSQL Table
title: operations
description: '12 columns: emerglevel, respphase, opsstatus, coordcenter, opsstartdate, estdurationdays, priorityrank, resourceallocstate, supplyflowstate. Joins to disasterevents, distributionhubs.'
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
| `opsregistry` | character varying, primary key | A VARCHAR(20) primary key for each operations record (e.g., 'OPS0001'). |
| `opsdistref` | character varying | A VARCHAR(20) referencing DisasterEvents(DistRegistry), tying these operations to a disaster (e.g., 'DIST0001'). |
| `opshubref` | character varying | A VARCHAR(20) referencing DistributionHubs(HubRegistry), associating operations with a particular hub (e.g., 'HUB0001'). |
| `emerglevel` | USER-DEFINED | An enum (EmergLevel_enum) labeling the emergency level; possible values: 'Black', 'Orange', 'Red', 'Yellow'. |
| `respphase` | USER-DEFINED | An enum (RespPhase_enum) for the disaster response phase; possible values: 'Reconstruction', 'Recovery', 'Emergency', 'Initial'. |
| `opsstatus` | USER-DEFINED | An enum (OpsStatus_enum) showing the operation’s status; values: 'Completed', 'Scaling Down', 'Active', 'Planning'. |
| `coordcenter` | character varying | A VARCHAR(80) describing the coordination center or command location (e.g., 'Central Ops HQ'). |
| `opsstartdate` | date | A DATE indicating when operations began (e.g., '2025-04-01'). |
| `estdurationdays` | integer | An INT estimating how many days the operation will last (e.g., 30). |
| `priorityrank` | USER-DEFINED | An enum (PriorityRank_enum) defining the priority level; possible values: 'High', 'Medium', 'Low', 'Critical'. |
| `resourceallocstate` | USER-DEFINED | An enum (ResourceAllocState_enum) describing resource allocation; possible values: 'Limited', 'Critical', 'Sufficient'. |
| `supplyflowstate` | USER-DEFINED | An enum (SupplyFlowState_enum) indicating supply chain flow status; possible values: 'Disrupted', 'Stable', 'Strained'. |

# Joins

* `opsdistref` references `distregistry` in [disasterevents](/tables/disasterevents.md).
* `opshubref` references `hubregistry` in [distributionhubs](/tables/distributionhubs.md).

# Related knowledge

* [emerglevel](/knowledge/emerglevel.md)
* [respphase](/knowledge/respphase.md)
* [resourceallocstate](/knowledge/resourceallocstate.md)
* [Market Stability Index (MSI)](/knowledge/market-stability-index.md)
* [Critical Resource Shortage](/knowledge/critical-resource-shortage.md)
* [High-Risk Response Operation](/knowledge/high-risk-response-operation.md)
* [Response Time Effectiveness Ratio (RTER)](/knowledge/response-time-effectiveness-ratio.md)
* [Critical Resource Prioritization Need](/knowledge/critical-resource-prioritization-need.md)
* [Financial Vulnerability Zone](/knowledge/financial-vulnerability-zone.md)
* [Cross-Agency Coordination Crisis](/knowledge/cross-agency-coordination-crisis.md)
