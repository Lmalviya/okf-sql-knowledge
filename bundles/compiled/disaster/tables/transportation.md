---
type: PostgreSQL Table
title: transportation
description: '18 columns: vehiclecount, trucksavailable, helosavailable, boatsavailable, totaldeliverytons, dailydeliverytons, lastmilestatus, distributionpoints, avgdeliveryhours, deliverysuccessrate, routeoptstatus, fuelefficiencylpk, maintenancestate, vehiclebreakrate. Joins to disasterevents, distributionhubs, supplies.'
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
| `transportregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying the transportation record (e.g., 'TRANS0001'). |
| `transportdistref` | character varying | A VARCHAR(20) referencing DisasterEvents(DistRegistry) (e.g., 'DIST0001'). |
| `transporthubref` | character varying | A VARCHAR(20) referencing DistributionHubs(HubRegistry), linking transport to a hub (e.g., 'HUB0001'). |
| `transportsupref` | character varying | A VARCHAR(20) referencing Supplies(SupplyRegistry), connecting transport operations to supplies (e.g., 'SUP0001'). |
| `vehiclecount` | integer | An INT recording how many vehicles are assigned (e.g., 15). |
| `trucksavailable` | integer | An INT counting the number of trucks available (e.g., 5). |
| `helosavailable` | integer | An INTEGER specifying how many helicopters are available (e.g., 2). |
| `boatsavailable` | bigint | A BIGINT measuring how many boats can be used (e.g., 1). |
| `totaldeliverytons` | numeric | A DECIMAL(9,3) for the total cargo capacity in tons (e.g., 50.000). |
| `dailydeliverytons` | numeric | A DECIMAL(8,2) capturing daily delivery capacity in tons (e.g., 7.50). |
| `lastmilestatus` | USER-DEFINED | An enum (LastMileStatus_enum) indicating last-mile delivery progress; values: 'On Track', 'Delayed', 'Suspended'. |
| `distributionpoints` | integer | An INTEGER labeling how many drop-off or distribution points exist (e.g., 10). |
| `avgdeliveryhours` | numeric | A DECIMAL(5,2) measuring average hours per delivery route (e.g., 8.50). |
| `deliverysuccessrate` | numeric | A DECIMAL(7,3) describing the delivery success percentage (e.g., 95.200). |
| `routeoptstatus` | USER-DEFINED | An enum (RouteOptStatus_enum) describing routing optimization; values: 'In Progress', 'Optimized', 'Required'. |
| `fuelefficiencylpk` | numeric | A DECIMAL(6,3) logging liters of fuel used per km (e.g., 0.250). |
| `maintenancestate` | USER-DEFINED | An enum (MaintenanceState_enum) capturing maintenance status; values: 'Overdue', 'Up to Date', 'Due'. |
| `vehiclebreakrate` | numeric | A DECIMAL(4,1) measuring how often vehicles break down, as a rate (e.g., 2.5). |

# Joins

* `transportdistref` references `distregistry` in [disasterevents](/tables/disasterevents.md).
* `transporthubref` references `hubregistry` in [distributionhubs](/tables/distributionhubs.md).
* `transportsupref` references `supplyregistry` in [supplies](/tables/supplies.md).

# Related knowledge

* [lastmilestatus](/knowledge/lastmilestatus.md)
* [Operational Efficiency Index (OEI)](/knowledge/operational-efficiency-index.md)
* [Market Stability Index (MSI)](/knowledge/market-stability-index.md)
* [Logistics Performance Metric (LPM)](/knowledge/logistics-performance-metric.md)
* [Resource Optimization Opportunity](/knowledge/resource-optimization-opportunity.md)
* [Operational Excellence](/knowledge/operational-excellence.md)
* [Logistics Breakdown](/knowledge/logistics-breakdown.md)
* [Response Time Effectiveness Ratio (RTER)](/knowledge/response-time-effectiveness-ratio.md)
* [Resource Distribution Equity (RDE)](/knowledge/resource-distribution-equity.md)
* [Supply Chain Sustainability Index (SCSI)](/knowledge/supply-chain-sustainability-index.md)
* [Logistics Network Resilience (LNR)](/knowledge/logistics-network-resilience.md)
* [Logistics System Collapse Risk](/knowledge/logistics-system-collapse-risk.md)
* [Resource Distribution Inequity](/knowledge/resource-distribution-inequity.md)
* [Rapid Response Success Model](/knowledge/rapid-response-success-model.md)
