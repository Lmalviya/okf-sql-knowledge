---
type: PostgreSQL Table
title: regulatoryandmaintenance
description: '23 columns: maintflag, maintdatelast, maintdatenext, calibflag, calibdatelast, calibdatenext, docuflag, compscore, riskflag, incidents, resolveflag, respperson, contactno, contactemerg, inspectdatelast, inspectdatenext, inspectoutcome, correctactions, preventsteps, validflag, verifymethod. Joins to shipments, transportinfo.'
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_schema.txt
  title: vaccine schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_column_meaning_base.json
  title: vaccine column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `maintflag` | character varying | A VARCHAR(20) showing the maintenance status (e.g., ‘Overdue’, ‘Up to Date’, ‘Due’). |
| `maintdatelast` | date | A DATE indicating the date of the most recent maintenance operation. |
| `maintdatenext` | date | A DATE specifying the scheduled or expected date for the next maintenance. |
| `calibflag` | character varying | A VARCHAR(20) describing calibration status (e.g., ‘Expired’, ‘Valid’, ‘Due’). |
| `calibdatelast` | date | A DATE for the most recent calibration event. |
| `calibdatenext` | date | A DATE for the next scheduled calibration. |
| `docuflag` | character varying | A VARCHAR(20) indicating documentation completeness (e.g., 'Missing', 'Complete', 'Partial'). |
| `compscore` | real | A REAL number reflecting a compliance or condition score assigned to the shipment/vehicle. |
| `riskflag` | character varying | A VARCHAR(50) denoting risk level or category (e.g., ‘High Risk’, ‘Low Risk’, ‘Medium Risk’). |
| `incidents` | smallint | A SMALLINT counting the number of recorded incidents or violations. |
| `resolveflag` | character varying | A VARCHAR(50) specifying how or if those incidents were resolved. |
| `respperson` | character varying | A VARCHAR(100) naming the responsible person or officer in charge. |
| `contactno` | character varying | A VARCHAR(50) for the primary contact phone/ID. |
| `contactemerg` | character varying | A VARCHAR(50) for emergency contact phone/ID details. |
| `inspectdatelast` | date | A DATE showing when the last official inspection was completed. |
| `inspectdatenext` | date | A DATE specifying when the next inspection is scheduled or due. |
| `inspectoutcome` | character varying | A VARCHAR(50) describing the overall outcome or result of the last inspection. |
| `correctactions` | text | A TEXT field detailing corrective actions taken post-inspection or post-incident. |
| `preventsteps` | text | A TEXT field describing preventive measures planned or implemented. |
| `validflag` | character varying | A VARCHAR(20) indicating the current validity status (e.g., 'In Process', 'Validated', 'Failed'). |
| `verifymethod` | character varying | A VARCHAR(50) naming the verification method or standard used. |
| `shipgov` | character varying | A VARCHAR(20) foreign key referencing Shipments(ShipmentRegistry), linking this record to a shipment. |
| `vehgov` | character varying | A VARCHAR(20) foreign key referencing TransportInfo(VehicleReg), linking this record to a vehicle. |

# Joins

* `shipgov` references `shipmentregistry` in [shipments](/tables/shipments.md).
* `vehgov` references `vehiclereg` in [transportinfo](/tables/transportinfo.md).

# Related knowledge

* [Maintenance Compliance Score (MCS)](/knowledge/maintenance-compliance-score.md)
* [Maintenance Due](/knowledge/maintenance-due.md)
* [CompScore Value](/knowledge/compscore-value.md)
* [Days Overdue](/knowledge/days-overdue.md)
