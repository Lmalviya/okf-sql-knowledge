---
type: PostgreSQL Table
title: lightingandsafety
description: '14 columns: lightingstatus, lightingintensitypercent, externallightstatus, emergencylightstatus, emergencystopstatus, alarmstatus, safetysystemstatus, lifesupportstatus, oxygensupplystatus, medicalequipmentstatus, wastemanagementstatus, watersupplystatus, safetysensors. Joins to equipment.'
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
| `lighteqref` | character varying | A VARCHAR(70) foreign key referencing Equipment(EquipmentCode), associating lighting/safety data with equipment. |
| `lightingstatus` | USER-DEFINED | An enum (LightingStatus_enum) describing the internal lighting state (e.g., Off, On, Auto). |
| `lightingintensitypercent` | numeric | A DECIMAL(5,2) showing the brightness level as a percentage. |
| `externallightstatus` | USER-DEFINED | An enum (ExternalLightStatus_enum) indicating external lighting state (e.g., Off, On, Auto). |
| `emergencylightstatus` | USER-DEFINED | An enum (EmergencyLightStatus_enum) describing emergency lighting (e.g., On, Off, Testing). |
| `emergencystopstatus` | USER-DEFINED | An enum (EmergencyStopStatus_enum) for the emergency stop button state (e.g., Activated, Reset, Ready). |
| `alarmstatus` | USER-DEFINED | An enum (AlarmStatus_enum) describing the overall alarm state (e.g., Normal, Critical, Warning). |
| `safetysystemstatus` | USER-DEFINED | An enum (SafetySystemStatus_enum) describing the overarching safety system state (e.g., Fault, Active, Standby). |
| `lifesupportstatus` | USER-DEFINED | An enum (LifeSupportStatus_enum) indicating the status of life support (e.g., Warning, Critical, Normal). |
| `oxygensupplystatus` | USER-DEFINED | An enum (OxygenSupplyStatus_enum) showing oxygen supply level (e.g., Warning, Normal, Critical). |
| `medicalequipmentstatus` | USER-DEFINED | An enum (MedicalEquipmentStatus_enum) describing the medical equipment state (e.g., Normal, Critical, Warning). |
| `wastemanagementstatus` | USER-DEFINED | An enum (WasteManagementStatus_enum) for waste disposal system health (e.g., Critical, Warning, Normal). |
| `watersupplystatus` | USER-DEFINED | An enum (WaterSupplyStatus_enum) indicating water supply condition (e.g., Normal, Warning, Critical). |
| `safetysensors` | jsonb | JSONB column. Collects status data for safety-related detection systems, such as fire, smoke, and gas sensors. |

# JSON fields

* `safetysensors.fire_detection`: An enum (FireDetectionStatus_enum) specifying the fire detection system status (e.g., Normal, Alert, Fault).
* `safetysensors.smoke_detection`: An enum (SmokeDetectionStatus_enum) for the smoke detection system status (e.g., Fault, Alert, Normal).
* `safetysensors.co_detection`: An enum (CODetectionStatus_enum) indicating the carbon monoxide detection status (e.g., Fault, Alert, Normal).
* `safetysensors.gas_detection`: An enum (GasDetectionStatus_enum) describing the presence of gas detection alerts (e.g., Alert, Fault, Normal).

# Joins

* `lighteqref` references `equipmentcode` in [equipment](/tables/equipment.md).

# Related knowledge

* [Extreme Weather Readiness (EWR)](/knowledge/extreme-weather-readiness.md)
* [Critical Equipment](/knowledge/critical-equipment.md)
* [Sustainable Polar Operations (SPO)](/knowledge/sustainable-polar-operations.md)
* [Extreme Weather Readiness Status (EWRS)](/knowledge/extreme-weather-readiness-status.md)
