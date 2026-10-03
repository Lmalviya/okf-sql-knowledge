---
type: PostgreSQL Table
title: scanpointcloud
description: '10 columns: scanresolmm, pointdense, coverpct, totalpts, clouddense, lappct, noisedb, refpct. Joins to personnel, projects.'
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
| `crewref` | character | Full name: 'Operator Reference'. Explanation: Which operator is linked to this point cloud. Data type: CHAR(8). Example: 'OP4641'. |
| `arcref` | character varying | Full name: 'Project Reference'. Explanation: Project ID associated with this point cloud. Data type: VARCHAR(10). Example: 'PR7509'. |
| `scanresolmm` | numeric | Full name: 'Scan Resolution (mm)'. Explanation: Resolution of points in millimeters. Data type: NUMERIC(5,2). Example: 2.4. |
| `pointdense` | integer | Full name: 'Point Density (points/m²)'. Explanation: Density of points per square meter. Data type: INTEGER. Example: 42812. |
| `coverpct` | numeric | Full name: 'Coverage (%)'. Explanation: Surface coverage percentage. Data type: NUMERIC(4,1). Example: 91.2. |
| `totalpts` | bigint | Full name: 'Total Points'. Explanation: Overall number of points in the cloud. Data type: BIGINT. Example: 46562436. |
| `clouddense` | integer | Full name: 'Point-Cloud Density Code'. Explanation: A numeric code classifying point density. Data type: INTEGER. Possible categories: 9449, 431, 7553, 1746. |
| `lappct` | numeric | Full name: 'Overlap (%)'. Explanation: Overlap percentage among multiple scans. Data type: NUMERIC(4,1). Example: 31.3. |
| `noisedb` | numeric | Full name: 'Noise Level (dB)'. Explanation: Measured noise in decibels. Data type: NUMERIC(6,3). Example: 1.318. |
| `refpct` | numeric | Full name: 'Surface Reflectivity (%)'. Explanation: Reflectivity percentage of scanned surfaces. Data type: NUMERIC(4,1). Example: 65.4. |

# Joins

* `arcref` references `arcregistry` in [projects](/tables/projects.md).
* `crewref` references `crewregistry` in [personnel](/tables/personnel.md).

# Related knowledge

* [Scan Resolution Index (SRI)](/knowledge/scan-resolution-index.md)
* [Scan Coverage Effectiveness (SCE)](/knowledge/scan-coverage-effectiveness.md)
* [Point Cloud Density Ratio (PCDR)](/knowledge/point-cloud-density-ratio.md)
* [Scan Quality Score (SQS)](/knowledge/scan-quality-score.md)
* [Processing Efficiency Ratio (PER)](/knowledge/processing-efficiency-ratio.md)
* [Archaeological Documentation Completeness (ADC)](/knowledge/archaeological-documentation-completeness.md)
* [High Resolution Scan](/knowledge/high-resolution-scan.md)
* [Comprehensive Coverage](/knowledge/comprehensive-coverage.md)
* [ScanResolMm (Scan Resolution)](/knowledge/scanresolmm.md)
* [PointDense (Point Density)](/knowledge/pointdense.md)
* [NoiseDb (Noise Level)](/knowledge/noisedb.md)
* [CoverPct (Coverage Percentage)](/knowledge/coverpct.md)
* [Scan Time Efficiency (STE)](/knowledge/scan-time-efficiency.md)
* [Feature Extraction Efficiency (FEE)](/knowledge/feature-extraction-efficiency.md)
* [Registration Accuracy Ratio (RAR)](/knowledge/registration-accuracy-ratio.md)
* [Spatial Density Index (SDI)](/knowledge/spatial-density-index.md)
* [Mesh-to-Point Ratio (MPR)](/knowledge/mesh-to-point-ratio.md)
* [Digital Preservation Quality (DPQ)](/knowledge/digital-preservation-quality.md)
