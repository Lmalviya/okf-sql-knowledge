---
type: PostgreSQL Table
title: bank_and_transactions
description: '15 columns: banktxfreq, banktxamt, bankrelscore, ovrfreq, bouncecount, inscoverage, lifeinsval, hlthinsstat, fraudrisk, idverscore, docverstat, kycstat, amlresult, chaninvdatablock. Joins to expenses_and_assets.'
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
| `bankexpref` | character varying, primary key | A VARCHAR(20) primary key referencing expenses_and_assets(ExpEmplRef). |
| `banktxfreq` | USER-DEFINED | An enum (BankTransactionFrequency_enum) describing transaction frequency (Low, Medium, High). |
| `banktxamt` | numeric | A DECIMAL(14,2) typical monthly transaction amount (e.g., '3000.00'). |
| `bankrelscore` | numeric | A NUMERIC(4,3) measuring the strength of the bank relationship (e.g., '0.850'). |
| `ovrfreq` | USER-DEFINED | An enum (OverdraftFrequency_enum) capturing overdraft occurrences (Frequent, Occasional, Rare, Never). |
| `bouncecount` | smallint | A SMALLINT for how many checks or payments have bounced (e.g., '1'). |
| `inscoverage` | USER-DEFINED | An enum (InsuranceCoverage_enum) for coverage level (Comprehensive, Basic). |
| `lifeinsval` | numeric | A DECIMAL(14,2) denoting total life insurance value (e.g., '50000.00'). |
| `hlthinsstat` | USER-DEFINED | An enum (HealthInsuranceStatus_enum) capturing health insurance (Basic, Premium). |
| `fraudrisk` | numeric | A DECIMAL(5,3) rating potential fraud risk (e.g., '0.120'). |
| `idverscore` | numeric | A DECIMAL(5,3) indicating identity verification confidence (e.g., '0.890'). |
| `docverstat` | USER-DEFINED | An enum (DocumentVerificationStatus_enum) describing document checks (Pending, Verified, Failed). |
| `kycstat` | USER-DEFINED | An enum (KYCStatus_enum) capturing KYC outcome (Pending, Failed, Completed). |
| `amlresult` | USER-DEFINED | An enum (AMLScreeningResult_enum) storing AML screening result (Flag, Pass, Fail). |
| `chaninvdatablock` | jsonb | JSONB column. Packs together digital‑channel habits and investment/trading style flags for engagement and cross‑sell scoring. |

# JSON fields

* `chaninvdatablock.onlineuse`: An enum (OnlineBankingUsage_enum) describing online banking use (High, Medium, Low).
* `chaninvdatablock.mobileuse`: An enum (MobileBankingUsage_enum) describing mobile banking usage (High, Medium, Low).
* `chaninvdatablock.autopay`: An enum (YesNo_enum) indicating if automatic payments are active (Yes, No).
* `chaninvdatablock.depostat`: An enum (YesNo_enum) indicating direct deposit usage (Yes, No).
* `chaninvdatablock.invcluster.investport`: An enum (InvestmentPortfolio_enum) labeling investment portfolio style (Conservative, Moderate, Aggressive).
* `chaninvdatablock.invcluster.investexp`: An enum (InvestmentExperience_enum) capturing investing experience (Extensive, Moderate, Limited).
* `chaninvdatablock.invcluster.tradeact`: An enum (TradingActivity_enum) describing trading activity (High, Medium, Low).

# Joins

* `bankexpref` references `expemplref` in [expenses_and_assets](/tables/expenses_and_assets.md).

# Related knowledge

* [Customer Engagement Score (CES)](/knowledge/customer-engagement-score.md)
* [Financially Vulnerable](/knowledge/financially-vulnerable.md)
* [Digital First Customer](/knowledge/digital-first-customer.md)
* [Investment Focused](/knowledge/investment-focused.md)
* [Over-Extended](/knowledge/over-extended.md)
* [Investment Portfolio Quality (IPQ)](/knowledge/investment-portfolio-quality.md)
* [Banking Relationship Strength (BRS)](/knowledge/banking-relationship-strength.md)
* [Digital Channel Opportunity](/knowledge/digital-channel-opportunity.md)
* [Credit Building Opportunity](/knowledge/credit-building-opportunity.md)
