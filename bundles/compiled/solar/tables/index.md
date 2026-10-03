# PostgreSQL Table

* [alerts](alerts.md) - 10 columns: alertmoment, alertstat, alertcnt, maintprior, replaceprior, optpotential. Joins to panel, performance, plant.
* [electrical](electrical.md) - 15 columns: iscinita, isccurra, vocinitv, voccurrv, impinita, impcurra, vmpinitv, vmpcurrv, ffactorinit, ffactorcurr, seriesresohm, shuntresohm. Joins to panel, performance.
* [environment](environment.md) - 18 columns: envmoment, celltempc, ambtempc, soillosspct, dustdengm2, cleancycledays, lastcleandt, relhumpct, windspdms, winddirdeg, preciptmm, airpresshpa, uv_idx, cloudcovpct, snowcovpct, irradiance_conditions. Joins to plant.
* [inverter](inverter.md) - 8 columns: invertmoment, inverttempc, gridvolt, gridfreqhz, pwrqualidx, power_metrics. Joins to plant.
* [maintenance](maintenance.md) - 14 columns: inspectmeth, inspectres, inspectdate, maintsched, wtystatus, wtyclaimcnt, maintcostusd, cleancostusd, replacecostusd, revlossusd. Joins to panel, performance, plant.
* [panel](panel.md) - 9 columns: panemfr, paneline, panetype, powratew, paneeffpct, nomtempc, tempcoef. Joins to plant.
* [performance](performance.md) - 6 columns: perfmoment, measpoww, powlossw, efficiency_profile. Joins to panel.
* [plant](plant.md) - 4 columns: growalias, gencapmw, initdate.
