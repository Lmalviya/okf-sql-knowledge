# Business Rule

* [Controller Overload Risk](controller-overload-risk.md) - Indicates robots with stressed controllers.
* [Cycle Efficiency Category](cycle-efficiency-category.md) - Categorizes robots based on their program cycle efficiency performance
* [Energy Inefficient Robot](energy-inefficient-robot.md) - Flags robots with poor energy efficiency.
* [Escalating Maintenance Costs](escalating-maintenance-costs.md) - Identifies robots with rising maintenance costs.
* [Fast Robot](fast-robot.md) - Indicates if the robot operates at high speed based on average TCP speed.
* [Heavily Used Robot](heavily-used-robot.md) - Indicates if the robot has been heavily used based on total operating hours.
* [High Cycle Count Robot](high-cycle-count-robot.md) - Indicates if the robot has a high total program cycle count.
* [High Fault Risk](high-fault-risk.md) - Indicates if the robot has a high risk of fault based on average fault prediction score.
* [High Safety Concern](high-safety-concern.md) - Flags robots with significant safety incidents.
* [High Temperature Joint 1](high-temperature-joint-1.md) - Indicates if Joint 1 has a high average temperature.
* [Joint Health Risk](joint-health-risk.md) - Indicates robots at risk of joint failure.
* [Maintenance Priority Level](maintenance-priority-level.md) - Classifies robots into maintenance priority categories based on fault prediction scores and remaining useful life
* [Multi-Operation Robot](multi-operation-robot.md) - Indicates if the robot has performed multiple operations.
* [Old Robot](old-robot.md) - Indicates if a robot is old based on its age.
* [Operational Instability](operational-instability.md) - Identifies robots with unstable joint performance.
* [Overheating Risk](overheating-risk.md) - Indicates if there is a risk of overheating based on maximum joint temperature.
* [Overloaded Robot](overloaded-robot.md) - Flags robots operating near or beyond payload capacity.
* [Precision Category](precision-category.md) - Categorizes the precision of the robot based on average position error.
* [Tool Replacement Status](tool-replacement-status.md) - Classifies robots into tool replacement priority categories based on tool wear rate and program cycles
* [Urgent Maintenance Needed](urgent-maintenance-needed.md) - Indicates if urgent maintenance is needed based on minimum Remaining Useful Life.

# Calculation

* [APE Rank](ape-rank.md) - Ranks the Average Position Error within each controller type to assess relative precision.
* [Average Cycle Time](average-cycle-time.md) - Calculates the average time in seconds for completing one program cycle
* [Average Joint 1 Temperature (AJ1T)](average-joint-1-temperature.md) - Calculates the average temperature of Joint 1 across all operations for a specific robot.
* [Average Position Error (APE)](average-position-error.md) - Calculates the average position error across all actuations for a specific robot.
* [Average TCP Speed (ATCS)](average-tcp-speed.md) - Calculates the average speed of the Tool Center Point across all actuations for a specific robot.
* [Controller Stress Index (CSI)](controller-stress-index.md) - Measures controller stress based on load and thermal metrics.
* [EER Rank](eer-rank.md) - Ranks the Energy Efficiency Ratio within each application type to assess relative efficiency.
* [Efficiency Metrics](efficiency-metrics.md) - Aggregates efficiency-related metrics, including the most efficient program and average program Operation Cycle Efficiency.
* [Energy Efficiency Ratio (EER)](energy-efficiency-ratio.md) - Measures energy efficiency by comparing energy usage to operating hours.
* [JDI-TOH Regression Slope](jdi-toh-regression-slope.md) - Measures the linear relationship between Joint Degradation Index and Total Operating Hours using regression.
* [Joint Degradation Index (JDI)](joint-degradation-index.md) - Computes a composite index of joint health based on temperature and vibration.
* [Joint Torque Variance (JTV)](joint-torque-variance.md) - Calculates the variance of joint torques to assess operational stability.
* [Maintenance Cost Trend (MCT)](maintenance-cost-trend.md) - Estimates the trend in maintenance costs over time.
* [Maximum Joint Temperature (MJT)](maximum-joint-temperature.md) - Finds the maximum temperature recorded for any joint across all operations for a specific robot.
* [Minimum Remaining Useful Life (MRUL)](minimum-remaining-useful-life.md) - Finds the minimum Remaining Useful Life across all maintenance records for a specific robot.
* [Model Average Max Operating Hours](model-average-max-operating-hours.md) - The average of the maximum Total Operating Hours recorded for each robot within a specific model series.
* [Model Average Position Error](model-average-position-error.md) - The average of the Average Position Error values for all robots within a specific model series.
* [Model Average TCP Speed](model-average-tcp-speed.md) - The average of the Average TCP Speed values for all robots within a specific model series.
* [Number of Operations (NO)](number-of-operations.md) - Counts the number of operation records for a specific robot.
* [Operation Cycle Efficiency (OCE)](operation-cycle-efficiency.md) - Calculates the efficiency of program cycles relative to cycle time.
* [Payload Utilization Ratio (PUR)](payload-utilization-ratio.md) - Measures how close the robot operates to its payload capacity.
* [Program Efficiency Rank](program-efficiency-rank.md) - Ranks programs based on their average Operation Cycle Efficiency across robots.
* [Recent Fault Prediction Score (RFPS)](recent-fault-prediction-score.md) - The fault prediction score from the most recent maintenance record for a robot.
* [Robot Age in Years (RAY)](robot-age-in-years.md) - Calculates the age of the robot in years based on installation date and record timestamp.
* [Robot Count](robot-count.md) - The number of distinct robots within a specific group (e.g., model series).
* [Safety Incident Score (SIS)](safety-incident-score.md) - Aggregates safety incidents from JSONB safety_metrics.
* [Tool Wear Rate (TWR)](tool-wear-rate.md) - Estimates the rate of tool wear relative to program cycles.
* [Total Operating Hours (TOH)](total-operating-hours.md) - The maximum total operating hours recorded for the robot across all operations.
* [Total Program Cycles (TPC)](total-program-cycles.md) - Sums the program cycle counts across all operations for a specific robot.
* [Weighted Fault Prediction Score (WFPS)](weighted-fault-prediction-score.md) - Calculates a weighted average fault prediction score, prioritizing recent records.

# Value Illustration

* [Controller Load](controller-load.md) - Illustrates the load value of the system controller.
* [Emergency Stops](emergency-stops.md) - Illustrates the number of emergency stops recorded.
* [Fault Prediction Score](fault-prediction-score.md) - Illustrates the fault prediction score in maintenance records.
* [Joint Temperature](joint-temperature.md) - Illustrates the temperature values of robot joints.
* [Position Error](position-error.md) - Illustrates the position error in robot actuations.
* [Remaining Useful Life (RUL)](remaining-useful-life.md) - Illustrates the Remaining Useful Life in maintenance records.
* [Safety State](safety-state.md) - Illustrates the safety state of the robot.
* [TCP Speed](tcp-speed.md) - Illustrates the speed of the Tool Center Point.
* [Tool Wear Percentage](tool-wear-percentage.md) - Illustrates the tool wear percentage.
* [Vibration Level](vibration-level.md) - Illustrates the vibration levels of robot joints.
