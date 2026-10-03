# PostgreSQL Table

* [articles](articles.md) - 21 columns: catlabel, subcatlbl, pubtime, authname, srcref, wordlen, readsec, difflevel, freshscore, qualscore, sentscore, contrscore, tagset, conttype, contformat, accscore, mediacount, vidsec, paywall, engagement_metrics. Joins to users.
* [devices](devices.md) - 9 columns: devtype, brwtype, osver, appver, scrres, vpsize, conntype, netspd. Joins to users.
* [interactionmetrics](interactionmetrics.md) - 2 columns: interaction_behavior. Joins to interactions.
* [interactions](interactions.md) - 13 columns: artval, intts, evttype, seqval, agentval, clkts, clkpos, clktype, clksrc, clkctx, inttype. Joins to recommendations, sessions.
* [recommendations](recommendations.md) - 11 columns: alglabel, stratlabel, posval, recpage, recsec, recscore, confval, divval, novval, seryval. Joins to articles.
* [sessions](sessions.md) - 23 columns: seshstart, seshdur, seshviews, bncrate, seshdepth, engscore, seshrecs, seshclicks, ctrval, langcode, tzoffset, ipaddr, geoctry, georeg, geocity, expref, persver, recset, relscore, persacc, recutil. Joins to devices, users.
* [systemperformance](systemperformance.md) - 12 columns: perfts, resptime, loadscore, errcount, warncount, perfscore, cachestate, apiver, cliver, featset. Joins to devices, sessions.
* [users](users.md) - 10 columns: regmoment, typelabel, seglabel, substatus, subdays, ageval, gendlbl, occulbl, testgrp, user_preferences.
