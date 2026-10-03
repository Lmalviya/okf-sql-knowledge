---
type: PostgreSQL Table
title: environmentandhealth
description: '13 columns: envimpactrate, wastemanagementstate, recyclepct, carbontons, renewenergypct, waterqualityindex, sanitationcoverage, diseaserisk, medicalemergencycapacity, vaccinationcoverage, mentalhealthaid. Joins to disasterevents.'
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
| `envhealthregistry` | character varying, primary key | A VARCHAR(20) primary key identifying each environment and health record (e.g., 'ENVH0001'). |
| `envdistref` | character varying | A VARCHAR(20) referencing DisasterEvents(DistRegistry), linking environment/health data to an event (e.g., 'DIST0001'). |
| `envimpactrate` | USER-DEFINED | An enum (EnvImpactRate_enum) rating environmental impact; values: 'Low', 'High', 'Medium'. |
| `wastemanagementstate` | USER-DEFINED | An enum (WasteManagementState_enum) describing waste management capability; values: 'Adequate', 'Limited', 'Critical'. |
| `recyclepct` | numeric | A NUMERIC(4,1) capturing the recycling rate percentage (e.g., 10.5). |
| `carbontons` | numeric | A DECIMAL(10,3) counting carbon emissions in tons (e.g., 250.000). |
| `renewenergypct` | numeric | A NUMERIC(5,2) logging what percent of energy usage is renewable (e.g., 15.50). |
| `waterqualityindex` | numeric | A DECIMAL(5,2) measuring water quality (e.g., 80.25). |
| `sanitationcoverage` | numeric | A NUMERIC(7,3) representing sanitation coverage percentage (e.g., 92.500). |
| `diseaserisk` | USER-DEFINED | An enum (DiseaseRisk_enum) for disease outbreak threat; values: 'High', 'Medium', 'Low'. |
| `medicalemergencycapacity` | USER-DEFINED | An enum (MedicalEmergencyCapacity_enum) capturing medical emergency readiness; values: 'Adequate', 'Critical', 'Limited'. |
| `vaccinationcoverage` | numeric | A DECIMAL(6,3) showing percent of population vaccinated (e.g., 85.200). |
| `mentalhealthaid` | USER-DEFINED | An enum (MentalHealthAid_enum) measuring mental health support; values: 'Limited', 'Available'. |

# Joins

* `envdistref` references `distregistry` in [disasterevents](/tables/disasterevents.md).

# Related knowledge

* [Environmental Impact Factor (EIF)](/knowledge/environmental-impact-factor.md)
* [Public Health Resilience Score (PHRS)](/knowledge/public-health-resilience-score.md)
* [Sustainable Response Operation](/knowledge/sustainable-response-operation.md)
* [Public Health Emergency](/knowledge/public-health-emergency.md)
