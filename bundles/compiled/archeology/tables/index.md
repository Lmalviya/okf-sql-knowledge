# PostgreSQL Table

* [equipment](equipment.md) - 6 columns: equipform, equipdesign, equiptune, equipstatus, powerlevel.
* [personnel](personnel.md) - 4 columns: crewlabel, leadregistry, leadlabel.
* [projects](projects.md) - 5 columns: vesseltag, fundflux, authpin, authhalt.
* [scanconservation](scanconservation.md) - 7 columns: harmassess, curerank, structstate, intervhistory, priordocs. Joins to projects, sites.
* [scanenvironment](scanenvironment.md) - 10 columns: ambictemp, humepct, illumelux, geosignal, trackstatus, linkstatus, photomap, imgcount. Joins to equipment, sites.
* [scanfeatures](scanfeatures.md) - 10 columns: traitextract, traitcount, articount, structkind, matkind, huestudy, texturestudy, patternnote. Joins to equipment, sites.
* [scanmesh](scanmesh.md) - 9 columns: facetverts, facetfaces, facetresmm, texdist, texpix, uvmapqual, geomdeltamm. Joins to equipment, sites.
* [scanpointcloud](scanpointcloud.md) - 10 columns: scanresolmm, pointdense, coverpct, totalpts, clouddense, lappct, noisedb, refpct. Joins to personnel, projects.
* [scanprocessing](scanprocessing.md) - 20 columns: flowsoft, flowhrs, proccpu, memusagegb, procgpu, stashloc, safebak, datalevel, metabench, coordframe, elevref, remaingb, stationlink, camcal, lensdist, colortune, flowstage, fmtver. Joins to equipment, sites.
* [scanqc](scanqc.md) - 11 columns: accucheck, ctrlstate, valimeth, valistate, archstat, pubstat, copystat, refmention, remark. Joins to personnel, projects.
* [scanregistration](scanregistration.md) - 9 columns: logaccumm, refmark, ctrlpts, logmethod, transform, errscale, errvalmm. Joins to personnel, projects.
* [scans](scans.md) - 12 columns: chronotag, scancount, climtune, huecatch, fmtfile, gbsize, pressratio, spanmin. Joins to personnel, projects, sites.
* [scanspatial](scanspatial.md) - 10 columns: aream2, volm3, boxx, boxy, boxz, angleaz, angletilt, groundspan. Joins to personnel, projects.
* [sites](sites.md) - 19 columns: zonelabel, digunit, gridtrace, geox, geoy, heightm, depthc, phasefactor, guessdate, typesite, presstat, guardhint, entrystat, saferank, insurstat, riskeval, healtheval, envhaz.
