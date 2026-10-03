# PostgreSQL Table

* [account](account.md) - 9 columns: acctident, platident, plattype, acctcreatedate, acctagespan, acctstatus, acctcategory, authstatus.
* [contentbehavior](contentbehavior.md) - 18 columns: postnum, postfreq, postintvar, cntsimscore, cntuniqscore, cntdiverseval, cntlangnum, cnttopicent, hashusepat, hashratio, mentionpat, mentionratio, urlsharefreq, urldomdiv, mediaupratio, mediareratio. Joins to sessionbehavior.
* [messaginganalysis](messaginganalysis.md) - 13 columns: msgsimscore, msgfreq, msgtgtdiv, resptimepat, convnatval, sentvar, langsoph, txtuniq, keypatmatch, topiccoh. Joins to contentbehavior, networkmetrics.
* [moderationaction](moderationaction.md) - 24 columns: abuserepnum, violtypedist, susphist, warnnum, appealnum, linkacctnum, clustsize, clustrole, netinflscore, coordscore, authenscore, credscore, reputscore, trustval, impactval, monitorpriority, investstatus, actiontaken, reviewfreq, lastrevdate, nextrevdate. Joins to contentbehavior, securitydetection.
* [networkmetrics](networkmetrics.md) - 3 columns: network_engagement_metrics. Joins to sessionbehavior.
* [profile](profile.md) - 3 columns: profile_composition. Joins to account.
* [securitydetection](securitydetection.md) - 7 columns: detecttime, detectsource, lastupd, updfreqhrs, detection_score_profile. Joins to technicalinfo.
* [sessionbehavior](sessionbehavior.md) - 9 columns: logintimepat, loginfreq, loginlocvar, sesslenmean, sesscount, actregval, acttimedist. Joins to profile.
* [technicalinfo](technicalinfo.md) - 13 columns: regip, iprepscore, ipcountrynum, vpnratio, proxycount, torflag, devtotal, devtypedist, browserdiv, uaconsval. Joins to messaginganalysis, networkmetrics.
