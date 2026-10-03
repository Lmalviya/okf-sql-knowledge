---
type: PostgreSQL Table
title: employment_and_income
description: '21 columns: emplstat, empllen, joblabel, indsector, employerref, annlincome, mthincome, incverify, incstabscore, addincome, addincomesrc, hshincome, emplstable, indrisklvl, occrisklvl, incsrcrisk, georisk, demrisk, edulevel, debincratio. Joins to core_record.'
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_schema.txt
  title: credit schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_column_meaning_base.json
  title: credit column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `emplcoreref` | character varying, primary key | A VARCHAR(20) primary key referencing core_record(CoreRegistry). |
| `emplstat` | USER-DEFINED | An enum (EmploymentStatus_enum) for employment status (Self-employed, Employed, Unemployed, Retired). |
| `empllen` | smallint | A SMALLINT indicating length of employment in years (e.g., '5'). |
| `joblabel` | USER-DEFINED | An enum (JobTitle_enum) labeling the job (Manager, Teacher, Doctor, Other, Engineer). |
| `indsector` | USER-DEFINED | An enum (IndustrySector_enum) naming the sector (Education, Technology, Healthcare, Finance, Other). |
| `employerref` | text | A TEXT field storing the employer name (e.g., 'ABC Corp'). |
| `annlincome` | numeric | A DECIMAL(12,2) capturing annual income in currency units (e.g., '65000.00'). |
| `mthincome` | numeric | A DECIMAL(12,2) capturing monthly income (e.g., '5400.00'). |
| `incverify` | USER-DEFINED | An enum (IncomeVerification_enum) describing income verification status (Pending, Verified, Failed). |
| `incstabscore` | real | A REAL score of how stable the income is (e.g., '7.5'). |
| `addincome` | numeric | A DECIMAL(12,2) indicating additional income (e.g., '500.00'). |
| `addincomesrc` | USER-DEFINED | An enum (AdditionalIncomeSource_enum) for source of additional income (Investment, Rental, Part-time). |
| `hshincome` | numeric | A DECIMAL(12,2) capturing total household income (e.g., '90000.00'). |
| `emplstable` | smallint | A SMALLINT rating how stable the employment is (e.g., '4'). |
| `indrisklvl` | USER-DEFINED | An enum (Risk3_enum) indicating industry risk (Low, Medium, High). |
| `occrisklvl` | USER-DEFINED | An enum (Risk3_enum) indicating occupation risk (Low, Medium, High). |
| `incsrcrisk` | USER-DEFINED | An enum (Risk3_enum) for income source risk (Low, Medium, High). |
| `georisk` | USER-DEFINED | An enum (Risk3_enum) for geographic risk (Low, Medium, High). |
| `demrisk` | USER-DEFINED | An enum (Risk3_enum) capturing demographic risk (Low, Medium, High). |
| `edulevel` | USER-DEFINED | An enum (EducationLevel_enum) labeling education (Doctorate, High School, Master, Bachelor). |
| `debincratio` | numeric | A DECIMAL(5,3) for debt-to-income ratio (e.g., '0.320'). |

# Joins

* `emplcoreref` references `coreregistry` in [core_record](/tables/core_record.md).

# Related knowledge

* [Debt-to-Income Ratio (DTI)](/knowledge/debt-to-income-ratio.md)
* [Credit Health Score (CHS)](/knowledge/credit-health-score.md)
* [Financial Stability Index (FSI)](/knowledge/financial-stability-index.md)
* [Financially Vulnerable](/knowledge/financially-vulnerable.md)
* [Income Stability Score](/knowledge/income-stability-score.md)
* [Debt-to-Income Ratio Interpretation](/knowledge/debt-to-income-ratio-interpretation.md)
* [Financial Vulnerability Score (FVS)](/knowledge/financial-vulnerability-score.md)
* [Credit Utilization Alert](/knowledge/credit-utilization-alert.md)
* [Investment Services Target](/knowledge/investment-services-target.md)
