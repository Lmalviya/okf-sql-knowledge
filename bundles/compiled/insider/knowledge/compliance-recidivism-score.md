---
type: Calculation
title: Compliance Recidivism Score (CRS)
description: Calculates a score indicating the tendency for repeat compliance issues, adjusted for account age.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 5
---

# Definition

CRS = \frac{\text{prevviol}}{\text{Max}(1, \frac{\text{acctdays}}{365})} \text{ (joining compliancecase to trader via transactionrecord)}

# Columns used

* [trader](/tables/trader.md): `acctdays`
* [compliancecase](/tables/compliancecase.md): `prevviol`

# Used by

* [Problematic Compliance History](/knowledge/problematic-compliance-history.md)
* [Compliance Health Score (CHS)](/knowledge/compliance-health-score.md)
* [Chronic Compliance Violator](/knowledge/chronic-compliance-violator.md)
* [Recidivism Enforcement Severity (RES)](/knowledge/recidivism-enforcement-severity.md)
