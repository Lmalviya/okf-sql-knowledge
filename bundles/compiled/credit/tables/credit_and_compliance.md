---
type: PostgreSQL Table
title: credit_and_compliance
description: '21 columns: sancresult, pepresult, legalstat, regcompliance, credscore, risklev, defhist, delinqcount, latepaycount, collacc, choffs, bankr, taxlien, civiljudge, credinq, hardinq, softinq, credrepdisp, credageyrs, oldaccage. Joins to bank_and_transactions.'
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
| `compbankref` | character varying, primary key | A VARCHAR(20) primary key referencing bank_and_transactions(BankExpRef). |
| `sancresult` | USER-DEFINED | An enum (SanctionsScreeningResult_enum) for sanctions screening (Fail, Flag, Pass). |
| `pepresult` | USER-DEFINED | An enum (PEPScreeningResult_enum) for PEP screening (Flag, Pass, Fail). |
| `legalstat` | USER-DEFINED | An enum (LegalStatus_enum) describing legal status (Clear, Under Review, Restricted). |
| `regcompliance` | USER-DEFINED | An enum (RegulatoryCompliance_enum) capturing compliance (Non-compliant, Compliant). |
| `credscore` | smallint | A SMALLINT holding the credit score (e.g., '720'). |
| `risklev` | USER-DEFINED | An enum (RiskLevel_enum) denoting risk level (Low, Medium, High, Very High). |
| `defhist` | USER-DEFINED | An enum (PaymentHistory_enum) indicating default history. Possible values: Poor, Fair, Good, Excellent, Current, Past. |
| `delinqcount` | smallint | A SMALLINT counting delinquencies (e.g., '2'). |
| `latepaycount` | smallint | A SMALLINT counting late payments (e.g., '1'). |
| `collacc` | integer | An INTEGER representing how many collection accounts (e.g., '0'). |
| `choffs` | smallint | A SMALLINT for number of charge-offs (e.g., '1'). |
| `bankr` | smallint | A SMALLINT indicating how many bankruptcies (e.g., '0'). |
| `taxlien` | smallint | A SMALLINT for any tax liens (e.g., '0'). |
| `civiljudge` | smallint | A SMALLINT counting civil judgments (e.g., '1'). |
| `credinq` | smallint | A SMALLINT for total credit inquiries (e.g., '3'). |
| `hardinq` | smallint | A SMALLINT for hard inquiries (e.g., '2'). |
| `softinq` | smallint | A SMALLINT for soft inquiries (e.g., '1'). |
| `credrepdisp` | character varying | A VARCHAR(50) capturing credit report disputes or notes (e.g., '2 disputes'). |
| `credageyrs` | smallint | A SMALLINT storing how many years of credit history (e.g., '10'). |
| `oldaccage` | smallint | A SMALLINT age in years of the oldest account (e.g., '15'). |

# Joins

* `compbankref` references `bankexpref` in [bank_and_transactions](/tables/bank_and_transactions.md).

# Related knowledge

* [Credit Health Score (CHS)](/knowledge/credit-health-score.md)
* [Risk-Adjusted Return (RAR)](/knowledge/risk-adjusted-return.md)
* [Prime Customer](/knowledge/prime-customer.md)
* [Financially Vulnerable](/knowledge/financially-vulnerable.md)
* [Credit Builder](/knowledge/credit-builder.md)
* [Frequent Credit Seeker](/knowledge/frequent-credit-seeker.md)
* [Credit Score Categories](/knowledge/credit-score-categories.md)
* [Risk Level Classifications](/knowledge/risk-level-classifications.md)
* [Payment History Quality](/knowledge/payment-history-quality.md)
* [Credit Quality Index (CQI)](/knowledge/credit-quality-index.md)
* [Credit Risk Intensity (CRI)](/knowledge/credit-risk-intensity.md)
* [Financial Stress Indicator](/knowledge/financial-stress-indicator.md)
* [Credit Building Opportunity](/knowledge/credit-building-opportunity.md)
* [Relationship Attrition Risk](/knowledge/relationship-attrition-risk.md)
