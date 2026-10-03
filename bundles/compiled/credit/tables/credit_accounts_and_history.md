---
type: PostgreSQL Table
title: credit_accounts_and_history
description: '21 columns: newaccage, avgaccage, accmixscore, credlimusage, payconsist, recentbeh, seekbeh, cardcount, totcredlimit, credutil, cardpayhist, loancount, activeloan, totloanamt, loanpayhist, custservint, complainthist, produsescore, chanusescore, custlifeval. Joins to credit_and_compliance.'
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
| `histcompref` | character varying, primary key | A VARCHAR(20) primary key referencing credit_and_compliance(CompBankRef). |
| `newaccage` | smallint | A SMALLINT for the newest account age in years (e.g., '1'). |
| `avgaccage` | numeric | A NUMERIC(4,1) for average account age (e.g., '4.5'). |
| `accmixscore` | numeric | A NUMERIC(4,3) measuring account mix (e.g., '0.765'). |
| `credlimusage` | numeric | A NUMERIC(4,3) ratio of used to available credit limit (e.g., '0.350'). |
| `payconsist` | numeric | A NUMERIC(4,3) capturing how consistent payments are (e.g., '0.900'). |
| `recentbeh` | USER-DEFINED | An enum (RecentCreditBehavior_enum) describing recent credit behavior (Stable, Improving, Deteriorating). |
| `seekbeh` | USER-DEFINED | An enum (CreditSeekingBehavior_enum) for seeking new credit (High, Medium, Low). |
| `cardcount` | smallint | A SMALLINT counting how many credit cards the user has (e.g., '2'). |
| `totcredlimit` | numeric | A DECIMAL(14,2) indicating total credit limit (e.g., '15000.00'). |
| `credutil` | numeric | A DECIMAL(5,3) capturing overall credit utilization (e.g., '0.350'). |
| `cardpayhist` | USER-DEFINED | An enum (PaymentHistory_enum) describing credit card payment history. Possible values: Poor, Fair, Good, Excellent, Current, Past. |
| `loancount` | smallint | A SMALLINT counting how many loan accounts exist (e.g., '2'). |
| `activeloan` | smallint | A SMALLINT indicating how many loans are active (e.g., '1'). |
| `totloanamt` | bigint | A BIGINT for total loan amount (e.g., '80000'). |
| `loanpayhist` | USER-DEFINED | An enum (PaymentHistory_enum) storing loan payment history. Possible values: Poor, Fair, Good, Excellent, Current, Past. |
| `custservint` | smallint | A SMALLINT for the number of customer service interactions (e.g., '2'). |
| `complainthist` | USER-DEFINED | An enum (ComplaintHistory_enum) labeling complaint history (Low, Medium, High). |
| `produsescore` | numeric | A NUMERIC(5,3) measuring how many financial products are used (e.g., '0.550'). |
| `chanusescore` | numeric | A NUMERIC(5,3) capturing channel usage diversity (e.g., '0.780'). |
| `custlifeval` | numeric | A DECIMAL(14,2) for the customer’s lifetime value (e.g., '12000.00'). |

# Joins

* `histcompref` references `compbankref` in [credit_and_compliance](/tables/credit_and_compliance.md).

# Related knowledge

* [Credit Utilization Ratio (CUR)](/knowledge/credit-utilization-ratio.md)
* [Customer Lifetime Value (CLV)](/knowledge/customer-lifetime-value.md)
* [Credit Health Score (CHS)](/knowledge/credit-health-score.md)
* [Customer Engagement Score (CES)](/knowledge/customer-engagement-score.md)
* [Account Health Index (AHI)](/knowledge/account-health-index.md)
* [High-Value Customer](/knowledge/high-value-customer.md)
* [Credit Builder](/knowledge/credit-builder.md)
* [Revolving Credit Dependent](/knowledge/revolving-credit-dependent.md)
* [Frequent Credit Seeker](/knowledge/frequent-credit-seeker.md)
* [Credit Utilization Impact](/knowledge/credit-utilization-impact.md)
* [Payment History Quality](/knowledge/payment-history-quality.md)
* [Account Mix Score Interpretation](/knowledge/account-mix-score-interpretation.md)
* [Customer Retention Risk (CRR)](/knowledge/customer-retention-risk.md)
* [Credit Health Momentum (CHM)](/knowledge/credit-health-momentum.md)
* [Credit Utilization Alert](/knowledge/credit-utilization-alert.md)
* [Digital Channel Opportunity](/knowledge/digital-channel-opportunity.md)
* [Relationship Attrition Risk](/knowledge/relationship-attrition-risk.md)
* [Cross-Sell Priority](/knowledge/cross-sell-priority.md)
