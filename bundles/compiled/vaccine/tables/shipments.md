---
type: PostgreSQL Table
title: shipments
description: '20 columns: timemark, routealign, customsflag, imppermitref, exppermitref, regprofile, insureflag, insureref, qualcheck, integritymark, contamlevel, sterilemark, packagestate, sealflag, sealref, tampersign, handlingguide, storagepose, generalnote.'
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
| `shipmentregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each shipment record in the database. |
| `timemark` | timestamp without time zone | A TIMESTAMP field indicating the exact date and time this shipment record was logged. |
| `routealign` | character varying | A VARCHAR(30) descriptor for the routing alignment or path code used by the shipment. |
| `customsflag` | USER-DEFINED | An enum (CustomsFlag_enum) representing the customs clearance status (e.g., 'Cleared', 'In Process', 'Pending'). |
| `imppermitref` | character varying | A VARCHAR(50) referencing the import permit number or identifier for the shipment. |
| `exppermitref` | character varying | A VARCHAR(50) referencing the export permit number or identifier for the shipment. |
| `regprofile` | character varying | A VARCHAR(50) signifying the regulatory or profile reference for this shipment. |
| `insureflag` | USER-DEFINED | An enum (InsuranceFlag_enum) capturing the insurance status (e.g., 'Active', 'Expired', 'Pending'). |
| `insureref` | character varying | A VARCHAR(50) referencing the insurance policy or coverage document number. |
| `qualcheck` | USER-DEFINED | An enum (QualityCheck_enum) indicating the quality check result (e.g., 'Failed', 'Passed', 'Pending'). |
| `integritymark` | USER-DEFINED | An enum (IntegrityStatus_enum) showing the shipment’s integrity status (e.g., 'Intact', 'Under Investigation', 'Compromised'). |
| `contamlevel` | USER-DEFINED | An enum (ContaminationRisk_enum) denoting potential contamination risk level (e.g., 'High', 'Low', 'Medium'). |
| `sterilemark` | USER-DEFINED | An enum (SterilityStatus_enum) indicating sterility status (e.g., 'Unknown', 'Compromised', 'Maintained'). |
| `packagestate` | USER-DEFINED | An enum (PackageCondition_enum) describing the package condition (e.g., 'Excellent', 'Fair', 'Poor', 'Good'). |
| `sealflag` | USER-DEFINED | An enum (SecuritySealStatus_enum) for the security seal status (e.g., 'Broken', 'Intact', 'Missing'). |
| `sealref` | character varying | A VARCHAR(50) referencing a security seal ID or documentation. |
| `tampersign` | USER-DEFINED | An enum (TamperEvidence_enum) noting tampering evidence (e.g., 'None Detected', 'Suspected', 'Confirmed'). |
| `handlingguide` | text | A TEXT field for special handling instructions or guidelines for the shipment. |
| `storagepose` | character varying | A VARCHAR(40) specifying how the shipment must be positioned or oriented during storage/transport. |
| `generalnote` | text | A TEXT field for any additional free-form notes regarding the shipment. |

# Related knowledge

* [Compromised Shipment](/knowledge/compromised-shipment.md)
* [Quality Compromise](/knowledge/quality-compromise.md)
