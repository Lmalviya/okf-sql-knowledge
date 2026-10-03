# PostgreSQL Table

* [actuation_data](actuation_data.md) - 29 columns: tcpxval, tcpyval, tcpzval, tcp_rxval, tcp_ryval, tcp_rzval, tcpspeedval, tcpaccelval, pathaccmmval, poserrmmval, orienterrdegval, payloadwval, payloadival, m1currval, m2currval, m3currval, m4currval, m5currval, m6currval, m1voltval, m2voltval, m3voltval, m4voltval, m5voltval, m6voltval. Joins to operation, robot_details, robot_record.
* [joint_condition](joint_condition.md) - 21 columns: j1tempval, j2tempval, j3tempval, j4tempval, j5tempval, j6tempval, j1vibval, j2vibval, j3vibval, j4vibval, j5vibval, j6vibval, j1backval, j2backval, j3backval, j4backval, j5backval, j6backval. Joins to operation, robot_details, robot_record.
* [joint_performance](joint_performance.md) - 4 columns: joint_metrics. Joins to operation, robot_details, robot_record.
* [maintenance_and_fault](maintenance_and_fault.md) - 11 columns: faultcodeval, issuecategoryval, issuelevelval, faultpredscore, faulttypeestimation, rulhours, upkeepduedays, upkeepcostest. Joins to actuation_data, operation, robot_details.
* [mechanical_status](mechanical_status.md) - 27 columns: brk1statval, brk2statval, brk3statval, brk4statval, brk5statval, brk6statval, enc1statval, enc2statval, enc3statval, enc4statval, enc5statval, enc6statval, gb1tempval, gb2tempval, gb3tempval, gb4tempval, gb5tempval, gb6tempval, gb1vibval, gb2vibval, gb3vibval, gb4vibval, gb5vibval, gb6vibval. Joins to actuation_data, operation, robot_details.
* [operation](operation.md) - 10 columns: totopshrval, apptypeval, opermodeval, currprogval, progcyclecount, cycletimesecval, axiscountval. Joins to robot_details, robot_record.
* [performance_and_safety](performance_and_safety.md) - 12 columns: conditionindexval, effectivenessindexval, qualitymeasureval, energyusekwhval, pwrfactorval, airpressval, toolchangecount, toolwearpct, safety_metrics. Joins to actuation_data, operation, robot_details.
* [robot_details](robot_details.md) - 9 columns: mfgnameval, modelseriesval, bottypeval, payloadcapkg, reachmmval, instdateval, fwversionval, ctrltypeval. Joins to robot_record.
* [robot_record](robot_record.md) - 3 columns: rects, botcode.
* [system_controller](system_controller.md) - 4 columns: controller_metrics. Joins to actuation_data, operation, robot_details.
