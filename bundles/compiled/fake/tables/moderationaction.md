---
type: PostgreSQL Table
title: moderationaction
description: '24 columns: abuserepnum, violtypedist, susphist, warnnum, appealnum, linkacctnum, clustsize, clustrole, netinflscore, coordscore, authenscore, credscore, reputscore, trustval, impactval, monitorpriority, investstatus, actiontaken, reviewfreq, lastrevdate, nextrevdate. Joins to contentbehavior, securitydetection.'
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_schema.txt
  title: fake schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_column_meaning_base.json
  title: fake column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `modactkey` | character, primary key | A CHAR(12) primary key uniquely identifying each moderation action record (e.g., 'MA0000001234'). |
| `masedetref` | character | A CHAR(12) referencing SecurityDetection(SecDetKey) (e.g., 'SD1234567890'). |
| `macntref` | character | A CHAR(12) referencing ContentBehavior(CntRef) (e.g., 'CB1234567890'). |
| `abuserepnum` | smallint | A SMALLINT counting how many abuse reports (e.g., '2'). |
| `violtypedist` | jsonb | A JSONB mapping violation types (e.g., '{"spam":5, "hate":1}'). |
| `susphist` | USER-DEFINED | An enum (SuspensionHistory_enum) detailing past suspensions (0 through 5). |
| `warnnum` | smallint | A SMALLINT showing how many warnings were issued (e.g., '1'). |
| `appealnum` | USER-DEFINED | An enum (AppealCount_enum) for how many appeals were filed (0 through 5). |
| `linkacctnum` | smallint | A SMALLINT counting linked/sockpuppet accounts (e.g., '3'). |
| `clustsize` | smallint | A SMALLINT representing the size of the related account cluster (e.g., '10'). |
| `clustrole` | USER-DEFINED | An enum (ClusterRole_enum) labeling the user’s cluster role (Isolated, Follower, Leader, Amplifier). |
| `netinflscore` | numeric | A NUMERIC(5,2) rating network influence (e.g., '7.85'). |
| `coordscore` | numeric | A NUMERIC(4,2) measuring coordinated behavior (e.g., '0.73'). |
| `authenscore` | numeric | A NUMERIC(5,3) rating authenticity (e.g., '0.745'). |
| `credscore` | numeric | A NUMERIC(4,1) rating credibility (e.g., '7.9'). |
| `reputscore` | numeric | A NUMERIC(5,4) user’s reputation measure (e.g., '0.8943'). |
| `trustval` | numeric | A NUMERIC(4,2) capturing trust level (e.g., '0.60'). |
| `impactval` | numeric | A NUMERIC(4,3) rating the potential impact of the violation (e.g., '1.034'). |
| `monitorpriority` | USER-DEFINED | An enum (MonitoringPriority_enum) indicating how closely to watch (Low, Medium, Urgent, High). |
| `investstatus` | USER-DEFINED | An enum (InvestigationStatus_enum) describing investigation status (Pending, Active, Completed). |
| `actiontaken` | USER-DEFINED | An enum (ActionTaken_enum) summarizing final moderation (Suspension, Warning, Restriction). |
| `reviewfreq` | USER-DEFINED | An enum (ReviewFrequency_enum) describing re-review frequency (Monthly, Quarterly, Daily, Weekly). |
| `lastrevdate` | date | A DATE showing last moderation review (e.g., '2025-03-20'). |
| `nextrevdate` | date | A DATE scheduling the next moderation review (e.g., '2025-04-20'). |

# Joins

* `macntref` references `cntref` in [contentbehavior](/tables/contentbehavior.md).
* `masedetref` references `secdetkey` in [securitydetection](/tables/securitydetection.md).

# Related knowledge

* [Content Authenticity Score (CAS)](/knowledge/content-authenticity-score.md)
* [Security Risk Score (SRS)](/knowledge/security-risk-score.md)
* [Profile Credibility Index (PCI)](/knowledge/profile-credibility-index.md)
* [Coordinated Activity Score (CAS)](/knowledge/coordinated-activity-score.md)
* [Moderation Priority Score (MPS)](/knowledge/moderation-priority-score.md)
* [Bot Network](/knowledge/bot-network.md)
* [Sockpuppet Network](/knowledge/sockpuppet-network.md)
* [Serial Violator](/knowledge/serial-violator.md)
* [Amplification Network](/knowledge/amplification-network.md)
* [moderationaction.coordscore](/knowledge/moderationaction-coordscore.md)
* [moderationaction.trustval](/knowledge/moderationaction-trustval.md)
* [moderationaction.impactval](/knowledge/moderationaction-impactval.md)
* [Coordinated Bot Risk (CBR)](/knowledge/coordinated-bot-risk.md)
* [Content Impact Score (CIS)](/knowledge/content-impact-score.md)
* [Network Influence Centrality (NIC)](/knowledge/network-influence-centrality.md)
* [Reputation Volatility Index (RVI)](/knowledge/reputation-volatility-index.md)
* [Network Synchronization Index (NSI)](/knowledge/network-synchronization-index.md)
* [Reputational Risk](/knowledge/reputational-risk.md)
* [High-Impact Amplifier](/knowledge/high-impact-amplifier.md)
* [maximum coordination score](/knowledge/maximum-coordination-score.md)
