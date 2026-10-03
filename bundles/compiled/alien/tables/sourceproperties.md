---
type: PostgreSQL Table
title: sourceproperties
description: '15 columns: sourceradeg, sourcedecdeg, sourcedistly, gallong, gallat, celestobj, objtype, objmag, objtempk, objmasssol, objagegyr, objmetal, objpropmotion, objradvel. Joins to signals.'
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_schema.txt
  title: alien schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_column_meaning_base.json
  title: alien column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `signalref` | character, primary key | Full name: 'Signal Registry Reference'. Explanation: Foreign key referencing the main signal. Data type: CHAR(36). Example: 'SIG-STU-5432'. |
| `sourceradeg` | numeric | Full name: 'Right Ascension (°)'. Explanation: RA of the source in degrees (0 to 360). Data type: DECIMAL(7,4). Example: '123.4567'. |
| `sourcedecdeg` | numeric | Full name: 'Declination (°)'. Explanation: Declination of the source in degrees (-90 to +90). Data type: DECIMAL(7,4). Example: '-20.4567'. |
| `sourcedistly` | numeric | Full name: 'Distance (ly)'. Explanation: Approximate distance to the source in light-years. Data type: NUMERIC(10,2). Example: '26000.45'. |
| `gallong` | numeric | Full name: 'Galactic Longitude (°)'. Explanation: Galactic longitude of the source. Data type: DECIMAL(6,2). Example: '12.34'. |
| `gallat` | numeric | Full name: 'Galactic Latitude (°)'. Explanation: Galactic latitude of the source. Data type: DECIMAL(6,2). Example: '-5.67'. |
| `celestobj` | character varying | Full name: 'Celestial Object'. Explanation: Broad classification of the object. Data type: VARCHAR(75). Possible categories: Galaxy, Planet, Star, Unknown. |
| `objtype` | character varying | Full name: 'Object Subtype'. Explanation: More specific object type. Data type: VARCHAR(50). Possible categories: Dwarf, Giant, Main Sequence, Unknown. |
| `objmag` | numeric | Full name: 'Apparent Magnitude'. Explanation: Brightness of the object as seen from Earth. Data type: NUMERIC(5,2). Example: '7.35'. |
| `objtempk` | integer | Full name: 'Object Temperature (K)'. Explanation: Approximate surface temperature in Kelvin. Data type: INTEGER. Example: '5800'. |
| `objmasssol` | numeric | Full name: 'Object Mass (solar)'. Explanation: Mass relative to the Sun. Data type: DECIMAL(6,3). Example: '1.005'. |
| `objagegyr` | numeric | Full name: 'Object Age (Gyr)'. Explanation: Estimated age in billions of years. Data type: DECIMAL(6,3). Example: '4.500'. |
| `objmetal` | numeric | Full name: 'Metallicity'. Explanation: Ratio of elements heavier than helium in the object. Data type: NUMERIC(5,3). Example: '0.012'. |
| `objpropmotion` | numeric | Full name: 'Proper Motion (mas/yr)'. Explanation: Apparent motion across the sky in milliarcseconds/year. Data type: DECIMAL(7,2). Example: '55.12'. |
| `objradvel` | numeric | Full name: 'Radial Velocity (km/s)'. Explanation: Speed at which the object is moving toward/away from us. Data type: DECIMAL(7,2). Example: '-23.45'. |

# Joins

* `signalref` references `signalregistry` in [signals](/tables/signals.md).

# Related knowledge

* [Celestial Location Significance Factor (CLSF)](/knowledge/celestial-location-significance-factor.md)
* [Habitable Zone Signal Relevance (HZSR)](/knowledge/habitable-zone-signal-relevance.md)
