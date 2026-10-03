---
type: PostgreSQL Table
title: scanmesh
description: '9 columns: facetverts, facetfaces, facetresmm, texdist, texpix, uvmapqual, geomdeltamm. Joins to equipment, sites.'
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
| `zoneref` | character varying | Full name: 'Site Reference'. Explanation: Associates mesh data with a site code. Data type: VARCHAR(12). Example: 'SC9016'. |
| `equipref` | character | Full name: 'Equipment Reference'. Explanation: Identifies which equipment was used to generate the mesh. Data type: CHAR(10). Example: 'SN20065'. |
| `facetverts` | bigint | Full name: 'Mesh Vertices'. Explanation: Count of mesh vertices. Data type: BIGINT. Example: 7234721. |
| `facetfaces` | bigint | Full name: 'Mesh Faces'. Explanation: Count of triangular or polygonal faces. Data type: BIGINT. Example: 5997318. |
| `facetresmm` | numeric | Full name: 'Mesh Resolution (mm)'. Explanation: Mesh vertex spacing in mm. Data type: NUMERIC(5,2). Example: 3.2. |
| `texdist` | character varying | Full name: 'Texture Resolution Setting'. Explanation: Preset texture resolution. Data type: VARCHAR(5). Possible categories: 2K, 1K, 4K. |
| `texpix` | integer | Full name: 'Texture Size (px)'. Explanation: Texture image dimension in pixels. Data type: INTEGER. Example: 2048. |
| `uvmapqual` | character varying | Full name: 'UV Mapping Quality'. Explanation: Quality of the UV mapping process. Data type: VARCHAR(10). Possible categories: Medium, High, Low. |
| `geomdeltamm` | numeric | Full name: 'Geometric Accuracy (mm)'. Explanation: Estimated geometric deviation in millimeters. Data type: NUMERIC(6,3). Example: 2.74. |

# Joins

* `equipref` references `equipregistry` in [equipment](/tables/equipment.md).
* `zoneref` references `zoneregistry` in [sites](/tables/sites.md).

# Related knowledge

* [Mesh Complexity Ratio (MCR)](/knowledge/mesh-complexity-ratio.md)
* [Texture Density Index (TDI)](/knowledge/texture-density-index.md)
* [Model Fidelity Score (MFS)](/knowledge/model-fidelity-score.md)
* [High Fidelity Mesh](/knowledge/high-fidelity-mesh.md)
* [GeomDeltaMm (Geometric Accuracy)](/knowledge/geomdeltamm.md)
* [Mesh-to-Point Ratio (MPR)](/knowledge/mesh-to-point-ratio.md)
* [Processing Resource Utilization (PRU)](/knowledge/processing-resource-utilization.md)
* [Resource-Intensive Model](/knowledge/resource-intensive-model.md)
