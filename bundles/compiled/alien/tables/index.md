# PostgreSQL Table

* [observationalconditions](observationalconditions.md) - 4 columns: obstime, obsdate, obsdurhrs. Joins to signals.
* [observatories](observatories.md) - 13 columns: weathprofile, seeingprofile, atmostransparency, lunarstage, lunardistdeg, solarstatus, geomagstatus, sidereallocal, airtempc, humidityrate, windspeedms, presshpa.
* [researchprocess](researchprocess.md) - 11 columns: analysisprio, followstat, peerrevstat, pubstat, resprio, fundstat, collabstat, secclass, discstat, notesmemo. Joins to signals.
* [signaladvancedphenomena](signaladvancedphenomena.md) - 9 columns: intermedeffects, gravlens, quanteffects, encryptevid, langstruct, msgcontent, cultsig, sciimpact. Joins to signals.
* [signalclassification](signalclassification.md) - 9 columns: sigclasstype, sigpattern, repeatcount, periodsec, complexidx, entropyval, infodense, classconf. Joins to signals.
* [signaldecoding](signaldecoding.md) - 13 columns: encodetype, compressratio, errcorrlvl, decodeconf, decodemethod, decodestat, decodeiters, proctimehrs, compresources, analysisdp, veriflvl, confirmstat. Joins to signals.
* [signaldynamics](signaldynamics.md) - 13 columns: sigintegrity, sigrecurr, sigevolve, tempstab, spatstab, freqstab, phasestab, ampstab, modstab, sigcoherence, sigdisp, sigscint. Joins to signals.
* [signalprobabilities](signalprobabilities.md) - 10 columns: falseposprob, sigunique, simindex, corrscore, anomscore, techsigprob, biosigprob, natsrcprob, artsrcprob. Joins to signals.
* [signals](signals.md) - 25 columns: timemark, detectinstr, signalclass, sigstrdb, freqmhz, bwhz, centerfreqmhz, freqdrifthzs, doppshifthz, sigdursec, pulsepersec, pulsewidms, modtype, modindex, carrierfreqmhz, phaseshiftdeg, polarmode, polarangledeg, snrratio, noisefloordbm, interflvl, rfistat, atmointerf. Joins to telescopes.
* [sourceproperties](sourceproperties.md) - 15 columns: sourceradeg, sourcedecdeg, sourcedistly, gallong, gallat, celestobj, objtype, objmag, objtempk, objmasssol, objagegyr, objmetal, objpropmotion, objradvel. Joins to signals.
* [telescopes](telescopes.md) - 14 columns: equipstatus, calibrstatus, pointaccarc, trackaccarc, focusquality, detecttempk, coolsysstatus, powerstatus, datastorstatus, netstatus, bandusagepct, procqueuestatus. Joins to observatories.
