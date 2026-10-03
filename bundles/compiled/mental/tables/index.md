# PostgreSQL Table

* [assessmentbasics](assessmentbasics.md) - 9 columns: atype, amethod, adurmin, alang, avalid, respconsist, symptvalid. Joins to patients.
* [assessmentsocialanddiagnosis](assessmentsocialanddiagnosis.md) - 20 columns: recstatus, socsup, faminv, relqual, workfunc, socfunc, adlfunc, strslvl, copskill, resscr, inlevel, motivlevel, primdx, secdx, dxdurm, prevhosp, lasthospdt, qolscr, funcimp. Joins to assessmentbasics.
* [assessmentsymptomsandrisk](assessmentsymptomsandrisk.md) - 9 columns: suicideation, suicrisk, selfharm, violrisk, subuse, subusefreq, subusesev, mental_health_scores. Joins to assessmentbasics.
* [clinicians](clinicians.md) - 11 columns: clinconf, assesslim, docustat, billcode, nxtrevdt, carecoord, refneed, fuptype, fupfreq. Joins to facilities.
* [encounters](encounters.md) - 11 columns: timemark, clinid, facid, missappt, txbarrier, nxapptdt, dqscore, assesscomplete. Joins to assessmentbasics, patients.
* [facilities](facilities.md) - 8 columns: rsource, envstress, lifeimpact, seasonpat, leglissue, ssystemchg, support_and_resources.
* [patients](patients.md) - 16 columns: patage, patgender, pateth, edulevel, empstat, maristat, livingarr, insurtype, insurstat, disabstat, housestable, cultfactor, stigmaimp, finstress. Joins to clinicians.
* [treatmentbasics](treatmentbasics.md) - 7 columns: curmed, medadh, medside, medchg, crisisint, therapy_details. Joins to encounters.
* [treatmentoutcomes](treatmentoutcomes.md) - 14 columns: thprog, txadh, txresp, sideburd, txgoalstat, recgoalstat, sympimp, funcimpv, workstatchg, satscr, theralliance, txeng, txsat. Joins to treatmentbasics.
