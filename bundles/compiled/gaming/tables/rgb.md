---
type: PostgreSQL Table
title: rgb
description: '9 columns: rgbbright, rgbcoloracc, rgbrfrate, rgbmodes, rgbzones, rgbcolors. Joins to audioandmedia, mechanical.'
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_schema.txt
  title: gaming schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_column_meaning_base.json
  title: gaming column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `rgbregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each RGB lighting record. |
| `rgbmechref` | character varying | A VARCHAR(20) foreign key referencing Mechanical(MechRegistry), associating RGB details with a mechanical record (e.g., a keyboard). |
| `rgbaudref` | character varying | A VARCHAR(20) foreign key referencing AudioAndMedia(AudRegistry), linking RGB details to audio/media data if necessary. |
| `rgbbright` | smallint | A SMALLINT indicating the RGB brightness level (on a predefined scale or percentage). |
| `rgbcoloracc` | numeric | A NUMERIC(4,1) measuring color accuracy or uniformity (e.g., Delta E or similar scale). |
| `rgbrfrate` | smallint | A SMALLINT specifying the refresh rate (in Hz) at which the RGB lighting updates. |
| `rgbmodes` | character varying | A VARCHAR(25) naming the different RGB lighting modes (e.g., 'Wave', 'Static', 'Breathing'). |
| `rgbzones` | smallint | A SMALLINT counting how many independent zones or sections of RGB control the device has. |
| `rgbcolors` | integer | An INTEGER for the total number of distinct colors supported (e.g., 16.8 million). |

# Joins

* `rgbaudref` references `audregistry` in [audioandmedia](/tables/audioandmedia.md).
* `rgbmechref` references `mechregistry` in [mechanical](/tables/mechanical.md).

# Related knowledge

* [RGB Implementation Quality (RIQ)](/knowledge/rgb-implementation-quality.md)
* [RgbZones (RGB Lighting Zones)](/knowledge/rgbzones.md)
