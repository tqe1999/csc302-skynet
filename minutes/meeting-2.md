# CSC302 Meeting Minutes - 01/10/2022

## Attendance
Taken by: Qi En 
Present: Henry (Kuan-Te), Chaoyu
Absent: None

## Agenda
Item | Description
--- | ---
Review | Run through past week's progress, research into possible datasets
Decide | Dataset
Decide | System requirement: Bash or Docker
Discuss | Implementation details
Decide | Workload distribution, next steps

## Discussion Items
Item | Decision | Considerations
--- | --- | ---
Bash/Docker | Decided to attempt to install Docker | Docker critical to ensuring repeatable deployment from images across environments, can bootstrap install from shell script, available across most Linux distros 
Vagrant | Defer pending research | Might be useful for testing on multiple platforms, but additional development overhead and may not be able to run using nested virtualization
Dataset | Use financial data | Simpler format and intuitive visualization compared to alternative suggestions like map of crimes. Might need to clarify doubts more often as not all members knowledgeable about finance

## Action Items
Item | By | Due
--- | --- | --- 
Documentation (packaging, CI/CD) | Qi En | 06/10/2022
Documentation (frontend) | Chaoyu | 06/10/2022
Documentation (backend, database) | Henry | 06/10/2022
Toy application | Qi En | 06/10/2022
Roadmap | Chaoyu, Henry | 06/10/2022