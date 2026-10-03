# PostgreSQL Table

* [advancedbehavior](advancedbehavior.md) - 6 columns: patsim, peercorr, mktcorr, secrotimp. Joins to transactionrecord.
* [compliancecase](compliancecase.md) - 21 columns: regfilestat, disclosecmp, brokrepstat, exchnotif, prevviol, comprate, risksc, alertlvl, invstprior, casestat, revfreq, lastrevdt, nextrevdt, monitint, survsys, detectmth, fposrate, modelconf. Joins to advancedbehavior, transactionrecord.
* [enforcementactions](enforcementactions.md) - 23 columns: acttake, esclvl, resstat, penimp, penamt, legactstat, settlestat, repimp, busrestr, remedstat, traderestr, sysupdneed, polupdneed, trainreq, repgenstat, dataretstat, auditstat, conflvl, accrestr, datashare. Joins to compliancecase, investigationdetails.
* [investigationdetails](investigationdetails.md) - 18 columns: reginv, patrecsc, behansc, netansc, relmapstat, connent, commaddr, sharectc, finrel, commpat, tcirclesz, grpbehsc, mktabprob, evidstr, docustat. Joins to compliancecase, sentimentandfundamentals.
* [sentimentandfundamentals](sentimentandfundamentals.md) - 16 columns: newsscore, socscore, anlycount, inholdpct, instownpct, shortintrt, optvolrt, putcallrt, impvolrank, unuoptact, corpeventprx, eventannotm, infoleaksc. Joins to trader, transactionrecord.
* [trader](trader.md) - 9 columns: tradekind, acctdays, acctbal, freqscope, voldaily, posavg, posspan, trading_performance.
* [transactionrecord](transactionrecord.md) - 12 columns: transtime, ordervar, ordertimepat, ordertypedist, cancelpct, modfreq, darkusage, offmkt, crossfreq, risk_indicators. Joins to trader.
