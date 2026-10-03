---
type: PostgreSQL Table
title: vaccinedetails
description: '11 columns: vacvariant, mfgsource, batchlabel, prodday, expireday, lotmeasure, vialtally, dosepervial, dosetotal. Joins to container, shipments.'
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
| `vacvariant` | character varying | A VARCHAR(50) naming the vaccine type or variant (e.g., ‘Viral Vector’, ‘mRNA’, ‘Inactivated’, ‘Protein Subunit’). |
| `mfgsource` | text | A TEXT field describing the manufacturer or source information of the vaccine. |
| `batchlabel` | character varying | A VARCHAR(50) specifying the batch or lot number label. |
| `prodday` | date | A DATE indicating the production/manufacture date of the vaccine batch. |
| `expireday` | date | A DATE specifying the vaccine’s expiration date. |
| `lotmeasure` | bigint | A BIGINT representing the quantity or measure of this vaccine lot (e.g., total units produced). |
| `vialtally` | smallint | A SMALLINT counting how many vials are included in this particular batch. |
| `dosepervial` | smallint | A SMALLINT indicating the number of individual doses contained in each vial. |
| `dosetotal` | integer | An INTEGER summing the total doses in this record (VialTally × DosePerVial). |
| `shipinject` | character varying | A VARCHAR(20) foreign key referencing Shipments(ShipmentRegistry), tying this vaccine detail to a shipment. |
| `containvac` | character varying | A VARCHAR(20) foreign key referencing Container(ContainRegistry), linking vaccine details to a specific container. |

# Joins

* `containvac` references `containregistry` in [container](/tables/container.md).
* `shipinject` references `shipmentregistry` in [shipments](/tables/shipments.md).

# Related knowledge

* [Vaccine Viability Period (VVP)](/knowledge/vaccine-viability-period.md)
* [Storage Efficiency Ratio (SER)](/knowledge/storage-efficiency-ratio.md)
* [VacVariant: 'Viral Vector'](/knowledge/vacvariant-viral-vector.md)
