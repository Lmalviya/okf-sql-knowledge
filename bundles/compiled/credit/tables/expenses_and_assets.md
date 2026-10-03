---
type: PostgreSQL Table
title: expenses_and_assets
description: '16 columns: mthexp, fixexpratio, discexpratio, savamount, investamt, liqassets, totassets, totliabs, networth, vehown, vehvalue, bankacccount, bankaccage, bankaccbal, propfinancialdata. Joins to employment_and_income.'
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
| `expemplref` | character varying, primary key | A VARCHAR(20) primary key referencing employment_and_income(EmplCoreRef). |
| `mthexp` | numeric | A DECIMAL(14,2) storing monthly expenses (e.g., '2000.00'). |
| `fixexpratio` | numeric | A DECIMAL(5,4) ratio for fixed expenses (e.g., '0.3000'). |
| `discexpratio` | numeric | A DECIMAL(5,4) ratio for discretionary expenses (e.g., '0.1500'). |
| `savamount` | numeric | A DECIMAL(14,2) capturing total savings (e.g., '15000.00'). |
| `investamt` | numeric | A DECIMAL(14,2) for total investments (e.g., '8000.00'). |
| `liqassets` | numeric | A DECIMAL(15,2) denoting liquid assets (e.g., '20000.00'). |
| `totassets` | numeric | A DECIMAL(15,2) for overall assets (e.g., '120000.00'). |
| `totliabs` | numeric | A DECIMAL(15,2) total liabilities (e.g., '40000.00'). |
| `networth` | numeric | A DECIMAL(15,2) net worth (assets − liabilities) (e.g., '80000.00'). |
| `vehown` | USER-DEFINED | An enum (VehicleOwnership_enum) for vehicle ownership (Lease, Own). |
| `vehvalue` | numeric | A DECIMAL(15,2) capturing vehicle value (e.g., '20000.00'). |
| `bankacccount` | smallint | A SMALLINT storing how many bank accounts are held (e.g., '2'). |
| `bankaccage` | smallint | A SMALLINT showing age in years of the oldest bank account (e.g., '5'). |
| `bankaccbal` | numeric | A DECIMAL(14,2) representing total bank account balances (e.g., '5000.00'). |
| `propfinancialdata` | jsonb | JSONB column. Bundles all housing‑related facts (ownership, value, and pay history) so risk or marketing rules need only one JSONB lookup. |

# JSON fields

* `propfinancialdata.propown`: An enum (PropertyOwnership_enum) describing property ownership (Rent, Living with Parents, Own).
* `propfinancialdata.proptype`: An enum (PropertyType_enum) for property classification (Apartment, House, Condo).
* `propfinancialdata.propvalue`: A DECIMAL(15,2) property value (e.g., '250000.00').
* `propfinancialdata.mortgagebits.mortbalance`: A DECIMAL(15,2) storing current mortgage balance (e.g., '150000.00').
* `propfinancialdata.mortgagebits.mortpayhist`: An enum (PaymentHistory_enum) for mortgage payment history. Possible values: Poor, Fair, Good, Excellent, Current, Past.
* `propfinancialdata.rentpayhist`: An enum (PaymentHistory_enum) for rent payment history. Possible values: Poor, Fair, Good, Excellent, Current, Past.

# Joins

* `expemplref` references `emplcoreref` in [employment_and_income](/tables/employment_and_income.md).

# Related knowledge

* [Loan-to-Value Ratio (LTV)](/knowledge/loan-to-value-ratio.md)
* [Net Worth](/knowledge/net-worth.md)
* [Financial Stability Index (FSI)](/knowledge/financial-stability-index.md)
* [Financially Vulnerable](/knowledge/financially-vulnerable.md)
* [Investment Focused](/knowledge/investment-focused.md)
* [Property Risk Exposure](/knowledge/property-risk-exposure.md)
* [Total Debt Service Ratio (TDSR)](/knowledge/total-debt-service-ratio.md)
* [Housing Affordability Ratio (HAR)](/knowledge/housing-affordability-ratio.md)
* [Financial Vulnerability Score (FVS)](/knowledge/financial-vulnerability-score.md)
* [Asset Liquidity Ratio (ALR)](/knowledge/asset-liquidity-ratio.md)
* [Investment Portfolio Quality (IPQ)](/knowledge/investment-portfolio-quality.md)
* [Mortgage Risk Profile](/knowledge/mortgage-risk-profile.md)
* [Premium Banking Candidate](/knowledge/premium-banking-candidate.md)
