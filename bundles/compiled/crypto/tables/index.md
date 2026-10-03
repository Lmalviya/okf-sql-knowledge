# PostgreSQL Table

* [accountbalances](accountbalances.md) - 7 columns: walletsum, availsum, frozensum, margsum, unrealline, realline. Joins to users.
* [analyticsindicators](analyticsindicators.md) - 3 columns: market_sentiment_indicators. Joins to marketdata, marketstats.
* [fees](fees.md) - 7 columns: feerange, feerate, feetotal, feecoin, rebrate, rebtotal. Joins to orders.
* [marketdata](marketdata.md) - 1 columns: quote_depth_snapshot.
* [marketstats](marketstats.md) - 19 columns: fundrate, fundspot, openstake, volday, tradeday, tnoverday, priceshiftday, highspotday, lowspotday, vwapday, mktsize, circtotal, totsupply, maxsupply, mkthold, traderank, liquidscore, volmeter. Joins to marketdata.
* [orderexecutions](orderexecutions.md) - 8 columns: fillcount, remaincount, fillquote, fillsum, expirespot, cancelnote, exectune. Joins to orders.
* [orders](orders.md) - 17 columns: recordvault, timecode, exchspot, mktnote, orderstamp, ordertune, dealedge, dealquote, dealcount, notionsum, orderflow, timespan, orderbase, clientmark, createspot, updatespot. Joins to users.
* [riskandmargin](riskandmargin.md) - 2 columns: risk_margin_profile. Joins to orders.
* [systemmonitoring](systemmonitoring.md) - 13 columns: apireqtotal, apierrtotal, apilatmark, wsstate, rateremain, lastupdnote, seqcode, slipratio, exectimespan, queueline, mkteffect, priceeffect. Joins to analyticsindicators.
* [users](users.md) - 2 columns: userstamp, acctscope.
