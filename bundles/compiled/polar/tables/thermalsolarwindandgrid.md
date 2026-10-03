---
type: PostgreSQL Table
title: thermalsolarwindandgrid
description: '17 columns: thermalimagingstatus, insulationstatus, heatlossratekwh, solarpanelstatus, windturbinestatus, powergridstatus, powerqualityindex, backuppowerstatus, fuelcellstatus, fuelcelloutputw, fuelcellefficiencypercent, hydrogenlevelpercent, oxygenlevelpercent, renewablemetrics. Joins to communication, equipment, powerbattery.'
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:09+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_schema.txt
  title: polar schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_column_meaning_base.json
  title: polar column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `thermaleqref` | character varying | A VARCHAR(70) foreign key referencing Equipment(EquipmentCode), linking this record to a piece of equipment that manages thermal or power generation. |
| `thermalcommref` | integer | An INTEGER foreign key referencing Communication(CommRegistry), relating thermal/power data to communication info if relevant. |
| `thermalimagingstatus` | USER-DEFINED | An enum (ThermalImagingStatus_enum) describing thermal imaging system health (e.g., Warning, Critical, Normal). |
| `insulationstatus` | USER-DEFINED | An enum (InsulationStatus_enum) indicating insulation quality (e.g., Fair, Poor, Good). |
| `heatlossratekwh` | numeric | A DECIMAL(8,3) measuring the heat loss rate in kilowatt-hours (kWh) per some reference time. |
| `solarpanelstatus` | USER-DEFINED | An enum (SolarPanelStatus_enum) describing the solar panel status (e.g., Fault, Inactive, Active). |
| `windturbinestatus` | USER-DEFINED | An enum (WindTurbineStatus_enum) indicating turbine operation state (e.g., Fault, Operating, Stopped). |
| `powergridstatus` | USER-DEFINED | An enum (PowerGridStatus_enum) describing grid connection state (e.g., Connected, Disconnected, Island Mode). |
| `powerqualityindex` | numeric | A DECIMAL(5,2) capturing power quality or stability (e.g., 95.50). |
| `backuppowerstatus` | USER-DEFINED | An enum (BackupPowerStatus_enum) for backup power system health (e.g., Fault, Active, Standby). |
| `fuelcellstatus` | USER-DEFINED | An enum (FuelCellStatus_enum) indicating the fuel cell’s operating state (e.g., Standby, Fault, Operating). |
| `fuelcelloutputw` | double precision | A DOUBLE PRECISION value denoting power output (in watts) from the fuel cell. |
| `fuelcellefficiencypercent` | numeric | A DECIMAL(4,1) describing the fuel cell’s efficiency as a percentage. |
| `hydrogenlevelpercent` | numeric | A DECIMAL(5,2) measuring the hydrogen supply level as a percentage of capacity. |
| `oxygenlevelpercent` | numeric | A DECIMAL(5,2) indicating the oxygen supply level as a percentage of capacity. |
| `thermalpowerref` | integer | An INTEGER foreign key referencing PowerBattery(PowerBattRegistry), connecting thermal/power generation data to battery/power details. |
| `renewablemetrics` | jsonb | JSONB column. Groups performance data for renewable energy sources, including solar panels and wind turbines. |

# JSON fields

* `renewablemetrics.solar.output_w`: A NUMERIC(9,2) specifying current solar panel output in watts.
* `renewablemetrics.solar.efficiency_percent`: A DECIMAL(5,2) showing the efficiency of the solar panel as a percentage.
* `renewablemetrics.solar.temperature_c`: A FLOAT for the solar panel’s temperature in Celsius.
* `renewablemetrics.wind.output_w`: A REAL value measuring the turbine’s power output in watts.
* `renewablemetrics.wind.rpm`: A SMALLINT specifying the wind turbine’s rotational speed in RPM.

# Joins

* `thermalcommref` references `commregistry` in [communication](/tables/communication.md).
* `thermaleqref` references `equipmentcode` in [equipment](/tables/equipment.md).
* `thermalpowerref` references `powerbattregistry` in [powerbattery](/tables/powerbattery.md).

# Related knowledge

* [Thermal Insulation Efficiency (TIE)](/knowledge/thermal-insulation-efficiency.md)
* [Renewable Energy Contribution (REC)](/knowledge/renewable-energy-contribution.md)
* [Extreme Weather Readiness (EWR)](/knowledge/extreme-weather-readiness.md)
* [fuelcellefficiencypercent](/knowledge/fuelcellefficiencypercent.md)
* [Emergency Response Readiness Status (ERRS)](/knowledge/emergency-response-readiness-status.md)
* [Polar Base Energy Security Status (PBESS)](/knowledge/polar-base-energy-security-status.md)
* [Comprehensive Environmental Adaptability Rating (CEAR)](/knowledge/comprehensive-environmental-adaptability-rating.md)
* [Extreme Weather Readiness Status (EWRS)](/knowledge/extreme-weather-readiness-status.md)
