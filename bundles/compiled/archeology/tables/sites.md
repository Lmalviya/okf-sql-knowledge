---
type: PostgreSQL Table
title: sites
description: '19 columns: zonelabel, digunit, gridtrace, geox, geoy, heightm, depthc, phasefactor, guessdate, typesite, presstat, guardhint, entrystat, saferank, insurstat, riskeval, healtheval, envhaz.'
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_schema.txt
  title: archeology schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_column_meaning_base.json
  title: archeology column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `zoneregistry` | character varying, primary key | Full name: 'Site Code'. Explanation: Primary key for a site. Data type: VARCHAR(12). Example: 'SC9016'. |
| `zonelabel` | text | Full name: 'Site Name'. Explanation: Descriptive name or label for the site. Data type: TEXT. Example: 'Site-North Alexanderville'. |
| `digunit` | character varying | Full name: 'Excavation Unit'. Explanation: Designation of a specific trench or unit. Data type: VARCHAR(8). Example: 'Unit-C9'. |
| `gridtrace` | character varying | Full name: 'Grid Reference'. Explanation: Grid or coordinate notation for the site location. Data type: VARCHAR(12). Example: 'S29-E8'. |
| `geox` | numeric | Full name: 'Latitude'. Explanation: Geographic latitude in decimal degrees. Data type: NUMERIC(8,5). Example: -9.60213. |
| `geoy` | numeric | Full name: 'Longitude'. Explanation: Geographic longitude in decimal degrees. Data type: NUMERIC(8,5). Example: -2.75641. |
| `heightm` | numeric | Full name: 'Altitude (m)'. Explanation: Elevation above sea level, in meters. Data type: NUMERIC(7,1). Example: 4391.4. |
| `depthc` | numeric | Full name: 'Depth (cm)'. Explanation: Depth measurement in centimeters. Data type: NUMERIC(7,1). Example: 329.9. |
| `phasefactor` | character varying | Full name: 'Cultural/Historical Period'. Explanation: Indicates the archaeological or historical phase. Data type: VARCHAR(25). Possible categories: Iron Age, Medieval, Classical, Bronze Age. |
| `guessdate` | character varying | Full name: 'Estimated Date'. Explanation: Approximate or labeled date (BCE/CE). Data type: VARCHAR(20). Possible categories: -2929 BCE, 1335 BCE, -4985 BCE, -3387 BCE. |
| `typesite` | character varying | Full name: 'Site Type'. Explanation: Classification of the site. Data type: VARCHAR(25). Possible categories: Burial, Industrial, Military, Settlement, Religious. |
| `presstat` | character varying | Full name: 'Preservation Status'. Explanation: Condition of preservation at the site. Data type: VARCHAR(25). Possible categories: Excellent, Fair, Critical, Good, Poor. |
| `guardhint` | character | Full name: 'Weather Protection'. Explanation: Indicates if the site is protected from weather. Data type: CHAR(5). Possible categories: None, Temporary. |
| `entrystat` | character varying | Full name: 'Site Access Status'. Explanation: Access restrictions or availability of the site. Data type: VARCHAR(8). Possible categories: Closed, Restricted, Open. |
| `saferank` | character varying | Full name: 'Security Level'. Explanation: Level of security or safety at the site. Data type: VARCHAR(15). Possible categories: Minimal, High, Standard. |
| `insurstat` | character varying | Full name: 'Insurance Status'. Explanation: Whether the site is insured, pending, or expired. Data type: VARCHAR(15). Possible categories: Expired, Pending. |
| `riskeval` | text | Full name: 'Risk Assessment Status'. Explanation: Status of risk evaluation for the site. Data type: TEXT. Possible categories: Required, Completed, Pending. |
| `healtheval` | character varying | Full name: 'Health and Safety Status'. Explanation: Indicates health/safety approvals. Data type: VARCHAR(12). Possible categories: Approved, Review, Pending. |
| `envhaz` | character | Full name: 'Environmental Risk'. Explanation: Rating of environmental hazards. Data type: CHAR(6). Possible categories: Low, Medium, High. |

# Related knowledge

* [Degradation Risk Zone](/knowledge/degradation-risk-zone.md)
* [Digital Conservation Priority](/knowledge/digital-conservation-priority.md)
* [PhaseFactor (Cultural Period)](/knowledge/phasefactor.md)
* [GuessDate (Estimated Dating)](/knowledge/guessdate.md)
* [Conservation Priority Index (CPI)](/knowledge/conservation-priority-index.md)
* [High Temporal Value Site](/knowledge/high-temporal-value-site.md)
