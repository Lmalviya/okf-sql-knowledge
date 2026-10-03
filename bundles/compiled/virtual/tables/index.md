# PostgreSQL Table

* [additionalnotes](additionalnotes.md) - 3 columns: noteinfo. Joins to retentionandinfluence.
* [commerceandcollection](commerceandcollection.md) - 9 columns: merchbuy, merchspendusd, digown, physown, collcomprate, tradelevel. Joins to engagement, membershipandspending.
* [engagement](engagement.md) - 12 columns: socintscore, engrate, actfreq, peaktime, actdayswk, avgsesscount, contpref, langpref, transuse. Joins to interactions, membershipandspending.
* [eventsandclub](eventsandclub.md) - 5 columns: clubjdate, participation_summary. Joins to membershipandspending, socialcommunity.
* [fans](fans.md) - 7 columns: nicklabel, regmoment, tierstep, ptsval, statustag, personal_attributes.
* [interactions](interactions.md) - 14 columns: timemark, actkind, actplat, platused, devtype, appver, giftfreq, gifttot, giftvalusd, favgifttag, engagement_metrics. Joins to fans, virtualidols.
* [loyaltyandachievements](loyaltyandachievements.md) - 8 columns: rankpos, inflscore, reputelv, trustval, reward_progress. Joins to engagement, eventsandclub.
* [membershipandspending](membershipandspending.md) - 7 columns: membkind, membdays, spendusd, spendfreq, paymethod. Joins to fans.
* [moderationandcompliance](moderationandcompliance.md) - 11 columns: rptcount, warncount, violhist, modstat, contcomp, ageverif, payverif, idverif. Joins to interactions, socialcommunity.
* [preferencesandsettings](preferencesandsettings.md) - 20 columns: privset, dsconsent, notifpref, commpref, markpref, langset, accessset, devcount, logfreq, lastlogdt, sesscount, timehrs, avgdailymin, peaksess, intconsist, platstable, connqual. Joins to membershipandspending, socialcommunity.
* [retentionandinfluence](retentionandinfluence.md) - 10 columns: churnflag, reactcount, refcount, contreach, viralcont, trendpart, hashuse. Joins to engagement, loyaltyandachievements.
* [socialcommunity](socialcommunity.md) - 5 columns: collabcount, community_engagement. Joins to commerceandcollection, engagement.
* [supportandfeedback](supportandfeedback.md) - 12 columns: techissuerpt, supptix, fbsubs, survpart, betapart, featreqsubs, bugsubs, satrate, npsval. Joins to interactions, preferencesandsettings.
* [virtualidols](virtualidols.md) - 7 columns: nametag, kindtag, debdate, assocgroup, genretag, primlang.
