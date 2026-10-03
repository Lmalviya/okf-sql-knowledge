---
type: PostgreSQL Table
title: core_record
description: '26 columns: timemark, clientref, appref, modelline, scoredate, nextcheck, dataqscore, confscore, overridestat, overridenote, decidestat, decidedate, agespan, gendlabel, maritalform, depcount, resdform, addrstab, phonestab, emailstab, clientseg, tenureyrs, crossratio, profitscore, churnrate.'
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
| `coreregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each core record (e.g., 'CRD001234'). |
| `timemark` | timestamp without time zone | A TIMESTAMP(6) indicating when the record was created (e.g., '2025-02-19 14:23:15.123456'). |
| `clientref` | character varying | A VARCHAR(20) referencing the customer ID (e.g., 'CUST00987'). |
| `appref` | character varying | A VARCHAR(20) referencing the application ID (e.g., 'APP001122'). |
| `modelline` | character varying | A VARCHAR(10) storing the model or version reference (e.g., '1.2'). |
| `scoredate` | date | A DATE capturing when scoring took place (e.g., '2025-02-19'). |
| `nextcheck` | date | A DATE noting the next review date (e.g., '2026-02-19'). |
| `dataqscore` | numeric | A NUMERIC(5,3) tracking data quality (e.g., '0.975'). |
| `confscore` | numeric | A NUMERIC(5,3) indicating confidence in the model’s output (e.g., '0.835'). |
| `overridestat` | USER-DEFINED | An enum (OverrideStatus_enum) describing override status (Policy, Manual). |
| `overridenote` | USER-DEFINED | An enum (OverrideReason_enum) capturing why an override occurred (Policy Exception, Management Decision). |
| `decidestat` | USER-DEFINED | An enum (DecisionStatus_enum) storing the final decision (Pending, Rejected, Approved). |
| `decidedate` | date | A DATE recording when the final decision was made (e.g., '2025-02-19'). |
| `agespan` | smallint | A SMALLINT for the customer’s age in years (e.g., '35'). |
| `gendlabel` | USER-DEFINED | An enum (Gender_enum) for gender (M, F). |
| `maritalform` | USER-DEFINED | An enum (MaritalStatus_enum) capturing marital status (Single, Married, Widowed, Divorced). |
| `depcount` | smallint | A SMALLINT counting how many dependents (e.g., '2'). |
| `resdform` | USER-DEFINED | An enum (ResidentialStatus_enum) describing residency (Temporary, Permanent, Foreign). |
| `addrstab` | smallint | A SMALLINT indicating address stability (e.g., '5'). |
| `phonestab` | smallint | A SMALLINT for phone number stability (e.g., '3'). |
| `emailstab` | character varying | A VARCHAR(50) capturing email stability or validation result (e.g., 'Valid12m'). |
| `clientseg` | USER-DEFINED | An enum (CustomerSegment_enum) labeling the customer segment (Premium, Standard, Basic). |
| `tenureyrs` | smallint | A SMALLINT for how many years the customer has been with the institution (e.g., '4'). |
| `crossratio` | numeric | A NUMERIC(4,3) ratio measuring cross-sell opportunities (e.g., '0.275'). |
| `profitscore` | numeric | A NUMERIC(4,3) indicating profitability (e.g., '0.765'). |
| `churnrate` | numeric | A NUMERIC(4,3) risk of customer churn (e.g., '0.220'). |

# Related knowledge

* [Risk-Adjusted Return (RAR)](/knowledge/risk-adjusted-return.md)
* [High-Value Customer](/knowledge/high-value-customer.md)
* [Cross-Sell Ratio Meaning](/knowledge/cross-sell-ratio-meaning.md)
* [Churn Rate Significance](/knowledge/churn-rate-significance.md)
* [Customer Retention Risk (CRR)](/knowledge/customer-retention-risk.md)
* [Banking Relationship Strength (BRS)](/knowledge/banking-relationship-strength.md)
* [Cross-Sell Priority](/knowledge/cross-sell-priority.md)
