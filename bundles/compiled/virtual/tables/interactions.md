---
type: PostgreSQL Table
title: interactions
description: '14 columns: timemark, actkind, actplat, platused, devtype, appver, giftfreq, gifttot, giftvalusd, favgifttag, engagement_metrics. Joins to fans, virtualidols.'
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_schema.txt
  title: virtual schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_column_meaning_base.json
  title: virtual column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `activityreg` | character varying, primary key | A VARCHAR(20) primary key for each interaction record (e.g., 'ACT001'). |
| `timemark` | timestamp without time zone | A TIMESTAMP indicating when the interaction occurred. |
| `interactfanpivot` | character varying | A VARCHAR(20) FK referencing Fans(UserRegistry), indicating which fan was involved. |
| `interactidolpivot` | character varying | A VARCHAR(20) FK referencing VirtualIdols(EntityReg), showing which idol was involved. |
| `actkind` | USER-DEFINED | An enum (InteractionType_enum) describing the action (Vote, Comment, Share, Gift, Live Stream). |
| `actplat` | USER-DEFINED | An enum (InteractionPlatform_enum) for the platform used (YouTube, Twitter, Official App, TikTok). |
| `platused` | USER-DEFINED | An enum (PlatformUsed_enum) describing the device platform (Tablet, Mobile, Console, PC). |
| `devtype` | USER-DEFINED | An enum (DeviceType_enum) specifying the device type (Windows, iOS, Android, Mac). |
| `appver` | character varying | A VARCHAR(20) capturing the version of the app used (e.g., 'v2.3.1'). |
| `giftfreq` | USER-DEFINED | An enum (GiftSendingFrequency_enum) capturing how often gifts are sent (Often, Rarely, Never, Frequent). |
| `gifttot` | integer | An INT total count of gifts sent during this session/interaction (e.g., 3). |
| `giftvalusd` | numeric | A DECIMAL(10,2) total USD value of gifts (e.g., 15.50). |
| `favgifttag` | USER-DEFINED | An enum (FavoriteGiftType_enum) for the fan’s preferred gift type (Limited, Custom, Premium, Standard). |
| `engagement_metrics` | jsonb | JSONB column. Captures metrics related to fan engagement during interactions, such as session duration, live attendance, watch hours, and chat activity. |

# JSON fields

* `engagement_metrics.session.sessdurmin`: A SMALLINT measuring session duration in minutes (e.g., 45).
* `engagement_metrics.session.liveatt`: A SMALLINT counting how many live stream attendances happened in this session.
* `engagement_metrics.session.watchhrs`: A DECIMAL(6,1) specifying how many hours of content the fan watched (e.g., 2.5).
* `engagement_metrics.chat_activity.chatmsg`: An INT tally of messages sent in chat (e.g., 30).
* `engagement_metrics.chat_activity.chatlang`: An enum (ChatLang_enum) describing chat language usage (Mixed, Translation, English, Native).
* `engagement_metrics.chat_activity.msgtone`: An enum (MessageSentiment_enum) indicating the sentiment (Negative, Positive, Neutral).
* `engagement_metrics.chat_activity.emojicount`: An INT number of emoji used by the fan (e.g., 10).
* `engagement_metrics.chat_activity.stkcount`: An INT number of stickers used (e.g., 2).

# Joins

* `interactfanpivot` references `userregistry` in [fans](/tables/fans.md).
* `interactidolpivot` references `entityreg` in [virtualidols](/tables/virtualidols.md).

# Related knowledge

* [interactions.gifttot_interactions.giftvalusd](/knowledge/interactions-gifttot-interactions-giftvalusd.md)
* [Monetization Value (MV)](/knowledge/monetization-value.md)
* [Whale](/knowledge/whale.md)
* [Multi-Idol Supporter](/knowledge/multi-idol-supporter.md)
* [Gift Impact Quotient (GIQ)](/knowledge/gift-impact-quotient.md)
* [Engagement-Deficient Whale](/knowledge/engagement-deficient-whale.md)
