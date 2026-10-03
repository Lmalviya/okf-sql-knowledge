---
type: PostgreSQL Table
title: usagerecords
description: '25 columns: displayrotatesched, displaydurmonths, restperiodmonths, displayreqs, storagereqs, handlingreqs, transportreqs, packingreqs, resaccessfreq, publicdispfreq, loanfreq, handlefreq, docufreq, monitorfreq, assessfreq, maintfreq, inspectfreq, calibfreq, certstatus, compliancestatus, auditstatus, qualityctrlstatus. Joins to artifactscore, sensitivitydata, showcases.'
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_schema.txt
  title: museum schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_column_meaning_base.json
  title: museum column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `artrefused` | character | A CHAR(10) NOT NULL foreign key referencing ArtifactsCore(ArtRegistry), indicating which artifact is being used. |
| `showcaserefused` | character | A CHAR(12) foreign key referencing Showcases(ShowcaseReg) if a showcase is involved in the usage. |
| `sensdatalink` | bigint | A BIGINT foreign key referencing SensitivityData(SensitivityRegistry). Links usage requirements to known sensitivities. |
| `displayrotatesched` | character | A CHAR(20) describing how often the artifact is rotated (possible values: 'Permanent', 'Resting', 'Active'). |
| `displaydurmonths` | smallint | A SMALLINT indicating how many months the artifact is displayed in a single rotation. |
| `restperiodmonths` | smallint | A SMALLINT for how many months the artifact rests between rotations. |
| `displayreqs` | character varying | A VARCHAR(120) listing any special display requirements (possible values: 'Special', 'Standard', 'Custom'). |
| `storagereqs` | character varying | A VARCHAR(60) describing special storage requirements (possible values: 'Standard', 'Custom', 'Special'). |
| `handlingreqs` | character varying | A VARCHAR(80) specifying guidelines for handling (possible values: 'Custom', 'Special', 'Standard'). |
| `transportreqs` | text | A TEXT field detailing transport requirements (possible values: 'Custom', 'Special', 'Standard'). |
| `packingreqs` | character varying | A VARCHAR(90) summarizing packing methods (possible values: 'Custom', 'Special', 'Standard'). |
| `resaccessfreq` | character | A CHAR(10) indicating how often the artifact is accessed for research (possible values: 'Frequent', 'Rare', 'Occasional'). |
| `publicdispfreq` | character | A CHAR(15) describing how often the artifact goes on public display (possible values: 'Frequent', 'Occasional', 'Rare'). |
| `loanfreq` | character | A CHAR(12) specifying how frequently the artifact is loaned out (possible values: 'Occasional', 'Frequent', 'Rare'). |
| `handlefreq` | character | A CHAR(10) indicating how frequently the artifact is handled (possible values: 'Rare', 'Frequent', 'Occasional'). |
| `docufreq` | character varying | A VARCHAR(20) describing how often documentation is updated (possible values: 'Frequent', 'Rare', 'Occasional'). |
| `monitorfreq` | character varying | A VARCHAR(35) for how often the artifact is monitored (possible values: 'Monthly', 'Daily', 'Weekly'). |
| `assessfreq` | character | A CHAR(15) for the frequency of condition assessments (possible values: 'Monthly', 'Quarterly', 'Annually'). |
| `maintfreq` | character | A CHAR(15) indicating the maintenance schedule (possible values: 'Monthly', 'Weekly', 'Quarterly'). |
| `inspectfreq` | character | A CHAR(15) describing the routine inspection frequency (possible values: 'Weekly', 'Monthly', 'Daily'). |
| `calibfreq` | character | A CHAR(15) stating how often instruments are calibrated (possible values: 'Monthly', 'Quarterly', 'Annually'). |
| `certstatus` | character varying | A VARCHAR(40) noting any certification status (possible values: 'Expired', 'Current', 'Pending'). |
| `compliancestatus` | character varying | A VARCHAR(55) summarizing compliance (possible values: 'Non-compliant', 'Partial', 'Compliant'). |
| `auditstatus` | USER-DEFINED | A CHAR(10) indicating the result of a related audit (possible values: 'Passed', 'Pending', 'Failed'). |
| `qualityctrlstatus` | USER-DEFINED | A VARCHAR(70) describing quality control status (possible values: 'Failed', 'Passed', 'Review'). |

# Joins

* `artrefused` references `artregistry` in [artifactscore](/tables/artifactscore.md).
* `sensdatalink` references `sensitivityregistry` in [sensitivitydata](/tables/sensitivitydata.md).
* `showcaserefused` references `showcasereg` in [showcases](/tables/showcases.md).

# Related knowledge

* [Exhibition Rotation Priority Score (ERPS)](/knowledge/exhibition-rotation-priority-score.md)
