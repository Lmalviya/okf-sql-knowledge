---
type: PostgreSQL Table
title: transportinfo
description: '21 columns: vehiclekind, vehtempc, speedkm, distdonekm, distleftkm, eta, departsite, currentsite, destsite, gpsflag, latvalue, lonvalue, altmeter, locupdatemin, locupdatemark, transmode, carrlabel, carrcert. Joins to container, shipments.'
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
| `vehiclereg` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying the transport vehicle record. |
| `vehiclekind` | USER-DEFINED | An enum (VehicleKind_enum) describing the vehicle type (e.g., 'Refrigerated Truck', 'Cargo Aircraft', 'Reefer Container'). |
| `vehtempc` | real | A REAL number for the current measured temperature (°C) inside the vehicle. |
| `speedkm` | real | A REAL number specifying the vehicle’s current speed in km/h. |
| `distdonekm` | numeric | A NUMERIC(9,2) indicating the distance already traveled (in kilometers). |
| `distleftkm` | numeric | A NUMERIC(9,2) specifying the remaining distance (in kilometers) until destination. |
| `eta` | timestamp without time zone | A TIMESTAMP for the estimated time of arrival at the destination. |
| `departsite` | character varying | A VARCHAR(100) naming the departure location/site. |
| `currentsite` | character varying | A VARCHAR(100) for the current location or site. |
| `destsite` | character varying | A VARCHAR(100) naming the destination location/site. |
| `gpsflag` | USER-DEFINED | An enum (GPSTrackingStatus_enum) for GPS tracking status (e.g., 'Active', 'Lost', 'Limited'). |
| `latvalue` | double precision | A DOUBLE PRECISION value for the vehicle’s current latitude. |
| `lonvalue` | double precision | A DOUBLE PRECISION value for the vehicle’s current longitude. |
| `altmeter` | real | A REAL number denoting the vehicle’s altitude in meters above sea level. |
| `locupdatemin` | smallint | A SMALLINT specifying how frequently (in minutes) the vehicle’s location data is updated. |
| `locupdatemark` | timestamp without time zone | A TIMESTAMP noting the last recorded location update time. |
| `transmode` | USER-DEFINED | An enum (TransportMode_enum) indicating the mode of transport (e.g., 'Road', 'Rail', 'Air', 'Sea'). |
| `carrlabel` | text | A TEXT field with carrier or transporter identification/labeling information. |
| `carrcert` | character varying | A VARCHAR(50) referencing any carrier certification or license number. |
| `shiptransit` | character varying | A VARCHAR(20) foreign key referencing Shipments(ShipmentRegistry). Links vehicle to a shipment in transit. |
| `containtransit` | character varying | A VARCHAR(20) foreign key referencing Container(ContainRegistry). Links the vehicle to a container in transit. |

# Joins

* `containtransit` references `containregistry` in [container](/tables/container.md).
* `shiptransit` references `shipmentregistry` in [shipments](/tables/shipments.md).

# Related knowledge

* [Route Completion Percentage (RCP)](/knowledge/route-completion-percentage.md)
* [VehicleKind: 'Reefer Container'](/knowledge/vehiclekind-reefer-container.md)
* [GPSFlag: 'Active'](/knowledge/gpsflag-active.md)
