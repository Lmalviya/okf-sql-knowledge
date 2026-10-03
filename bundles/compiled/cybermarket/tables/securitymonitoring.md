---
type: PostgreSQL Table
title: securitymonitoring
description: '18 columns: securityauditstatus, vulntally, inctally, securitymeasurecount, encryptionstrength, authenticationmethod, sessionsecurityscore, dataprotectionlevel, privprotscore, operationalsecurityscore, fpprob, alertsev, alertcategory, alertconfidencescore, threat_analysis_metrics. Joins to communication, riskanalysis.'
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_schema.txt
  title: cybermarket schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_column_meaning_base.json
  title: cybermarket column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `secmonregistry` | character varying, primary key | Primary key (VARCHAR(30)) for a security monitoring record (e.g., 'SM-xyz123'). |
| `securityauditstatus` | USER-DEFINED | An enum (SecurityAuditStatus_enum) describing the system's last security audit result (Warning, Pass, Fail). |
| `vulntally` | smallint | A SMALLINT counting discovered vulnerabilities (e.g., 5). |
| `inctally` | smallint | A SMALLINT counting security incidents (e.g., 2). |
| `securitymeasurecount` | smallint | An INT listing how many security measures are in place (e.g., 8). |
| `encryptionstrength` | USER-DEFINED | An enum (EncryptionStrength_enum) describing encryption (Strong, Military-grade, Standard). |
| `authenticationmethod` | USER-DEFINED | An enum (AuthenticationMethod_enum) used for system auth (Basic, 2FA, Multi-factor). |
| `sessionsecurityscore` | numeric | A NUMERIC(5,2) (0–99.99) measuring session protection (e.g., 78.50). |
| `dataprotectionlevel` | USER-DEFINED | An enum (DataProtectionLevel_enum) reflecting data handling (Maximum, Enhanced, Basic). |
| `privprotscore` | numeric | A NUMERIC(5,2) rating privacy protections (e.g., 90.75). |
| `operationalsecurityscore` | numeric | A NUMERIC(5,2) rating OPSEC (e.g., 70.40). |
| `fpprob` | numeric | A NUMERIC(5,4) false-positive probability (0–0.9999) (e.g., 0.0345). |
| `alertsev` | USER-DEFINED | An enum (AlertSev_enum) for alert severity (Low, Medium, High, Critical). |
| `alertcategory` | USER-DEFINED | An enum (AlertCategory_enum) describing alert focus (Pattern, Transaction, Behavior, Security). |
| `alertconfidencescore` | numeric | A NUMERIC(4,2) (0–99.99) for confidence in each alert (e.g., 85.20). |
| `riskref` | character varying | FK referencing RiskAnalysis(RiskRegistry). Links monitoring data to a risk profile. |
| `commref` | character varying | FK referencing Communication(CommRegistry) if relevant security logs exist. |
| `threat_analysis_metrics` | jsonb | JSONB column. A collection of scores related to threat intelligence integration, detection capabilities, anonymity assessment, and analytical pattern matching from security monitoring. |

# JSON fields

* `threat_analysis_metrics.threat_intelligence_score`: A NUMERIC(5,2) measuring usage of threat intel (e.g., 85.20).
* `threat_analysis_metrics.detection_evasion_score`: A NUMERIC(5,2) for how well the system evades detection (e.g., 60.15).
* `threat_analysis_metrics.anonymity_level`: An enum (AnonLevel_enum) describing anonymity (Low, Medium, High).
* `threat_analysis_metrics.traceability_score`: A NUMERIC(5,3) (0–999.999) rating how traceable user actions are (e.g., 245.671).
* `threat_analysis_metrics.event_correlation_strength`: A NUMERIC(5,3) measuring cross-event correlation (e.g., 123.456).
* `threat_analysis_metrics.pattern_matching_score`: A NUMERIC(4,2) (0–99.99) for pattern-matching adequacy (e.g., 75.30).
* `threat_analysis_metrics.behavioral_analysis_score`: A NUMERIC(5,2) rating behavior-based threat detection (e.g., 88.25).
* `threat_analysis_metrics.ml_confidence_score`: A NUMERIC(5,3) ML detection confidence (0–999.999) (e.g., 567.842).
* `threat_analysis_metrics.anomaly_detection_score`: A NUMERIC(5,3) anomaly detection rating (e.g., 423.101).

# Joins

* `commref` references `commregistry` in [communication](/tables/communication.md).
* `riskref` references `riskregistry` in [riskanalysis](/tables/riskanalysis.md).

# Related knowledge

* [cybermarket|securitymonitoring|alertsev](/knowledge/cybermarket-securitymonitoring-alertsev.md)
* [Security Posture Score (SPS)](/knowledge/security-posture-score.md)
* [High-Security Entity](/knowledge/high-security-entity.md)
* [Market Vulnerability Index (MVI)](/knowledge/market-vulnerability-index.md)
* [Unstable Market](/knowledge/unstable-market.md)
