# Business Rule

* [Aggressive Event Speculator](aggressive-event-speculator.md) - Classifies event-driven traders who employ an aggressive risk strategy.
* [Chronic Compliance Violator](chronic-compliance-violator.md) - Identifies traders with a problematic history and a high recidivism score.
* [Collusion Network Indicator](collusion-network-indicator.md) - Suggests potential collusion based on investigation details.
* [Confirmed Evasive Layering/Spoofing](confirmed-evasive-layering-spoofing.md) - Identifies traders confirmed to be layering or spoofing who also exhibit high cancellation/modification behavior, suggesting deliberate evasion.
* [Confirmed Manipulator Under Scrutiny](confirmed-manipulator-under-scrutiny.md) - Identifies traders with confirmed manipulative patterns whose cases are under high scrutiny.
* [Costly High-Frequency Risk Enforcement](costly-high-frequency-risk-enforcement.md) - Identifies enforcement cases with significant financial impact against traders previously identified as high-frequency, high-risk.
* [Elevated Regulatory Scrutiny](elevated-regulatory-scrutiny.md) - Identifies compliance cases under intense review or investigation.
* [Escalated Compliance Failure](escalated-compliance-failure.md) - Identifies traders with a problematic compliance history who have now incurred significant enforcement actions.
* [Event-Driven Trader](event-driven-trader.md) - Classifies traders whose activity appears strongly linked to corporate events.
* [Financially Impactful Enforcement Case](financially-impactful-enforcement-case.md) - Identifies traders who faced significant enforcement actions with a high financial impact relative to their account size.
* [High Cancellation/Modification Trader](high-cancellation-modification-trader.md) - Identifies traders who frequently cancel or modify orders, potentially indicating manipulative intent or poor execution strategy.
* [High-Frequency High-Risk Trader](high-frequency-high-risk-trader.md) - Identifies traders classified as High-Risk who also operate at high frequency.
* [High-Intensity Insider Investigation](high-intensity-insider-investigation.md) - Flags investigations triggered by potential insider trading that show high intensity scores, suggesting significant findings.
* [High-Risk Collusion Group Member](high-risk-collusion-group-member.md) - Identifies traders within a suspected collusion network who individually exhibit high-risk behavior.
* [High-Risk Manipulator Candidate](high-risk-manipulator-candidate.md) - Identifies traders flagged for both high-risk profiles and specific market manipulation patterns.
* [High-Risk Trader Profile](high-risk-trader-profile.md) - Identifies traders exhibiting characteristics associated with high-risk trading strategies.
* [High-Scrutiny Wash Trading Case](high-scrutiny-wash-trading-case.md) - Identifies compliance cases involving high-volume wash trading concerns that are also under elevated regulatory scrutiny.
* [High SDLR Transaction](high-sdlr-transaction.md) - Identifies transactions deemed high-risk based on their Sentiment-Driven Leakage Risk score exceeding a specific threshold.
* [High Velocity Suspicion Trader](high-velocity-suspicion-trader.md) - Identifies traders exhibiting both high risk-adjusted turnover and a high suspicious activity index.
* [High-Volume Wash Trading Concern](high-volume-wash-trading-concern.md) - Flags traders with wash trading alerts who also trade significant volume.
* [Market Manipulation Pattern: Layering/Spoofing](market-manipulation-pattern-layering-spoofing.md) - Identifies trading sessions indicative of layering or spoofing tactics.
* [Networked Mimicry Risk](networked-mimicry-risk.md) - Flags traders suspected of peer mimicry who are also part of an identified potential collusion network.
* [Peer Mimicry Suspicion](peer-mimicry-suspicion.md) - Flags traders whose behavior closely matches peers but deviates little from known patterns, potentially mimicking a risky group.
* [Potential Insider Trading Flag](potential-insider-trading-flag.md) - Flags transactions potentially linked to insider knowledge based on timing and context.
* [Potentially Evasive Order Modifier](potentially-evasive-order-modifier.md) - Flags high cancellation/modification traders who make significant use of dark pools.
* [Premature Resolution Block](premature-resolution-block.md) - A business rule preventing an enforcement action from being marked as 'Resolved' if associated risk metrics (like III) exceed a predefined threshold, ensuring high-risk cases receive sufficient review.
* [Problematic Compliance History](problematic-compliance-history.md) - Identifies traders with a poor track record of compliance.
* [Severe Chronic Violator Case](severe-chronic-violator-case.md) - Identifies compliance cases under elevated scrutiny involving traders flagged as chronic compliance violators.
* [Significant Enforcement Action](significant-enforcement-action.md) - Categorizes enforcement actions that represent substantial penalties or restrictions.
* [Suspected Event-Driven Insider](suspected-event-driven-insider.md) - Flags traders identified as event-driven who also trigger potential insider trading alerts.
* [Volatile Event Speculator](volatile-event-speculator.md) - Flags aggressive event speculators whose trading coincides with high sentiment divergence, indicating potential reaction to conflicting information.
* [Wash Trading Alert](wash-trading-alert.md) - Flags transactions highly suspicious for wash trading.

# Calculation

* [Aggressive Suspicion Score (ASS)](aggressive-suspicion-score.md) - Combines overall suspicious activity index with aggressive trading intensity, identifying traders who are both suspicious and trade aggressively.
* [Aggressive Trading Intensity (ATI)](aggressive-trading-intensity.md) - Measures intensity by combining high turnover, leverage, and order modification frequency.
* [Boosted Insider Leakage Score (BILS)](boosted-insider-leakage-score.md) - Increases the Information Leakage Score if a Potential Insider Trading Flag is also present.
* [Capital-Adjusted Investigation Intensity (CAII)](capital-adjusted-investigation-intensity.md) - Normalizes the investigation intensity index by the trader's account balance, showing investigation focus relative to trader size.
* [Combined Manipulation Indicator (CMI)](combined-manipulation-indicator.md) - A combined score reflecting both general suspicious activity and specific pattern anomalies.
* [Compliance Health Score (CHS)](compliance-health-score.md) - Inverse score reflecting compliance history severity, penalizing high recidivism and poor ratings.
* [Compliance Recidivism Score (CRS)](compliance-recidivism-score.md) - Calculates a score indicating the tendency for repeat compliance issues, adjusted for account age.
* [Cross-Modification Ratio (CMR)](cross-modification-ratio.md) - Calculates the ratio of cross-trade frequency to order modification intensity, potentially indicating coordinated or manipulative crossing activity.
* [Daily Turnover Rate (DTR)](daily-turnover-rate.md) - Calculates the ratio of a trader's daily trading volume to their account balance, indicating capital velocity.
* [Enforcement Financial Impact Ratio (EFIR)](enforcement-financial-impact-ratio.md) - Calculates the ratio of the penalty amount to the trader's account balance at the time of the related transaction.
* [Insider Sentiment Short Ratio (ISSR)](insider-sentiment-short-ratio.md) - Combines boosted insider leakage score with relative short interest, identifying potential insider trading concurrent with high relative short interest.
* [Investigation Compliance Risk Index (ICRI)](investigation-compliance-risk-index.md) - Combines the weighted investigation score with the inverse compliance health score, highlighting cases that are both problematic and under intense investigation.
* [Investigation Intensity Index (III)](investigation-intensity-index.md) - Combines behavioral and network analysis scores from an investigation.
* [Logarithmic Enforcement Fine Impact (LEFI)](logarithmic-enforcement-fine-impact.md) - Calculates the log-scaled financial impact ratio of enforcement fines, emphasizing order of magnitude.
* [Market-Adjusted Pattern Anomaly (MAPA)](market-adjusted-pattern-anomaly.md) - Calculates pattern anomaly score adjusted for market correlation, highlighting non-market related deviations.
* [Market-Agnostic Suspicion Index (MASI)](market-agnostic-suspicion-index.md) - Combines the general suspicion index with market-adjusted pattern anomaly, focusing on suspicious activity independent of market moves.
* [Order Modification Intensity (OMI)](order-modification-intensity.md) - Measures how frequently a trader modifies orders relative to their cancellation rate.
* [Pattern Anomaly Score (PAS)](pattern-anomaly-score.md) - Measures the deviation of a trader's pattern similarity from their peer correlation, potentially indicating unique illicit behavior.
* [Peer Correlation Z-Score](peer-correlation-z-score.md) - A normalized score indicating how many standard deviations an individual record's peer correlation ('peercorr') is away from the average peer correlation of all traders within the same trader kind ('tradekind'). Used for standardized comparison across different peer groups.
* [Recidivism Enforcement Severity (RES)](recidivism-enforcement-severity.md) - Multiplies the compliance recidivism score by the enforcement financial impact, highlighting costly repeat offenders.
* [Relative Short Interest (RSI)](relative-short-interest.md) - Calculates short interest ratio relative to institutional ownership.
* [Risk-Adjusted Turnover (RAT)](risk-adjusted-turnover.md) - Calculates trader turnover scaled by their leverage exposure.
* [Risk-Adjusted Win Rate (RAWR)](risk-adjusted-win-rate.md) - Calculates the trader's historical win percentage adjusted for their leverage exposure.
* [Sentiment Divergence Factor (SDF)](sentiment-divergence-factor.md) - Measures the difference between news and social media sentiment scores.
* [Sentiment-Driven Leakage Risk (SDLR)](sentiment-driven-leakage-risk.md) - Calculates potential information leakage risk weighted by sentiment-driven unusual option volume.
* [Sentiment-Weighted Option Volume (SWOV)](sentiment-weighted-option-volume.md) - Adjusts the option volume ratio based on the divergence between news and social sentiment.
* [Suspicion-Weighted Turnover (SWT)](suspicion-weighted-turnover.md) - Calculates daily turnover weighted by the Suspicious Activity Index.
* [Suspicious Activity Index (SAI)](suspicious-activity-index.md) - A composite index attempting to quantify overall suspicious trading behavior based on risk indicators.
* [Trader Leverage Exposure (TLE)](trader-leverage-exposure.md) - Extracts the leverage ratio from the trader's performance data.
* [Unique Pattern Deviation Ratio (UPDR)](unique-pattern-deviation-ratio.md) - Measures the ratio of unique pattern deviation (anomaly) to the similarity with known illicit patterns, indicating how unusual the potentially illicit behavior is.
* [Weighted Investigation Score (WIS)](weighted-investigation-score.md) - Combines raw investigation scores with the current alert severity level.

# Value Illustration

* [Compliance Rating Grade](compliance-rating-grade.md) - Explains the overall compliance assessment grade assigned in compliance cases.
* [Dark Pool Usage Venues](dark-pool-usage-venues.md) - Explains the nature of dark pool usage indicated in transaction records.
* [Information Leakage Score Interpretation](information-leakage-score-interpretation.md) - Provides context for the information leakage score, indicating potential trading on non-public information.
* [Marking the Close Patterns](marking-the-close-patterns.md) - Explains the patterns associated with influencing the closing price of a security.
* [Momentum Ignition Signals](momentum-ignition-signals.md) - Explains the signals related to attempting to artificially create price momentum.
* [Off-Market Trading Activity](off-market-trading-activity.md) - Illustrates types of trading activity occurring outside public exchanges.
* [Order Type Distribution](order-type-distribution.md) - Illustrates the mix of primary order types used by a trader.
* [Pattern Similarity Score Context](pattern-similarity-score-context.md) - Provides context for the pattern similarity score, comparing trading to known illicit behaviors.
* [Trader Position Holding Style](trader-position-holding-style.md) - Illustrates the typical duration traders hold their positions, based on their strategy.
* [Trading Restriction Period Types](trading-restriction-period-types.md) - Explains the types of trading restrictions imposed as part of enforcement.
* [Unusual Option Activity Level](unusual-option-activity-level.md) - Illustrates the degree of detected unusual options trading volume or types.
