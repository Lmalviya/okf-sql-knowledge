# PostgreSQL Table

* [buyers](buyers.md) - 9 columns: buyspan, buytxtally, buyspending, buyfreqcat, buychecklvl, buyriskrate. Joins to markets, vendors.
* [communication](communication.md) - 18 columns: iptally, tornodecount, vpnflag, brwsrunique, devfpscore, connpatscore, encryptmethod, commchannel, msgtally, commfreq, langpattern, sentiscore, keymatchcount, susppatscore, riskindiccount. Joins to products, transactions.
* [investigation](investigation.md) - 20 columns: investstat, lawinterest, regrisklvl, compliancescore, investpriority, resptimemins, escalationlevel, casestatus, resolutiontimehours, actiontaken, followuprequired, reviewfrequency, nextreviewdate, notescount, dataretentionstatus, lastupdated, updatefrequencyhours. Joins to riskanalysis, securitymonitoring.
* [markets](markets.md) - 13 columns: mktdenom, mktclass, mktspan, sizecluster, dlyflow, mthactive, vendcount, buycount, listtotal, interscore, esccomprate, market_status_reputation.
* [products](products.md) - 8 columns: prodtheme, prodsubcat, prodlistdays, prodpriceusd, prodqty. Joins to buyers, vendors.
* [riskanalysis](riskanalysis.md) - 16 columns: fraudprob, moneyrisk, linkedtxcount, txchainlen, wallrisksc, wallage, wallbalusd, wallturnrt, txvel, profilecomplete, idverifyscore, feedbackauthscore, network_behavior_analytics. Joins to communication, transactions.
* [securitymonitoring](securitymonitoring.md) - 18 columns: securityauditstatus, vulntally, inctally, securitymeasurecount, encryptionstrength, authenticationmethod, sessionsecurityscore, dataprotectionlevel, privprotscore, operationalsecurityscore, fpprob, alertsev, alertcategory, alertconfidencescore, threat_analysis_metrics. Joins to communication, riskanalysis.
* [transactions](transactions.md) - 19 columns: rectag, eventstamp, paymethod, payamtusd, txfeeusd, escrowused, escrowhrs, multisigflag, txstatus, txfinishhrs, shipmethod, shipregionsrc, shipregiondst, crossborderflag, routecomplexity. Joins to buyers, markets, products.
* [vendors](vendors.md) - 11 columns: vendspan, vendrate, vendtxcount, vendsucccount, venddisputecount, vendplacecount, vendpaymethods, vendchecklvl, vendlastmoment. Joins to markets.
