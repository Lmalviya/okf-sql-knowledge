---
type: PostgreSQL Table
title: operationmaintenance
description: '13 columns: operationhours, maintenancecyclehours, lastmaintenancedate, nextmaintenancedue, operationalstatus, crewcertificationstatus, inspectionstatus, compliancestatus, documentationstatus, opmaintcommref, costmetrics. Joins to equipment, location.'
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:09+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_schema.txt
  title: polar schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_column_meaning_base.json
  title: polar column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `opmainteqref` | character varying | A VARCHAR(60) foreign key referencing Equipment(EquipmentCode), linking operational data to a specific equipment unit. |
| `opmaintlocref` | integer | An INTEGER foreign key referencing Location(LocationRegistry), associating this record with a location if applicable. |
| `operationhours` | numeric | A NUMERIC(8,3) indicating the total hours the equipment has been in operation. |
| `maintenancecyclehours` | numeric | A NUMERIC(7,2) for the planned hours between maintenance events. |
| `lastmaintenancedate` | date | A DATE noting when the last maintenance was performed. |
| `nextmaintenancedue` | date | A DATE indicating the scheduled date for the next maintenance. |
| `operationalstatus` | USER-DEFINED | An enum (OperationalStatus_enum) showing the current operating state (e.g., Storage, Standby, Repair, Active, Maintenance). |
| `crewcertificationstatus` | USER-DEFINED | An enum (CrewCertificationStatus_enum) indicating crew status (e.g., Valid, Pending, Expired). |
| `inspectionstatus` | USER-DEFINED | An enum (InspectionStatus_enum) for the result of any recent inspection (e.g., Failed, Passed, Pending). |
| `compliancestatus` | USER-DEFINED | An enum (ComplianceStatus_enum) describing overall compliance (e.g., Review, Non-compliant, Compliant). |
| `documentationstatus` | USER-DEFINED | An enum (DocumentationStatus_enum) indicating if documentation is (e.g., Updated, Incomplete, Complete). |
| `opmaintcommref` | integer | An INTEGER optionally linking to a record in Communication or another table if referenced (not enforced here). |
| `costmetrics` | jsonb | JSONB column. Aggregates financial metrics related to maintenance, repair, and operating costs. |

# JSON fields

* `costmetrics.maintenance_usd`: A DECIMAL(8,2) for the cost (in USD) of recent or typical maintenance.
* `costmetrics.repair_usd`: A DECIMAL(9,3) for the cost (in USD) of repairs, if any.
* `costmetrics.operating_usd`: A NUMERIC(9,4) indicating the ongoing operating cost (in USD).

# Joins

* `opmainteqref` references `equipmentcode` in [equipment](/tables/equipment.md).
* `opmaintlocref` references `locationregistry` in [location](/tables/location.md).

# Related knowledge

* [Operational Readiness Score (ORS)](/knowledge/operational-readiness-score.md)
* [Maintenance Priority Level](/knowledge/maintenance-priority-level.md)
* [operationhours](/knowledge/operationhours.md)
* [Long-term Operational Stability Score (LOSS)](/knowledge/long-term-operational-stability-score.md)
* [Polar Vehicle Safe Operation Conditions (PVSOC)](/knowledge/polar-vehicle-safe-operation-conditions.md)
