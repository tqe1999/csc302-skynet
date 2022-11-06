# CSC302 Meeting Minutes - 18/10/2022

## Attendance
Taken by: Henry (Kuan-Te)
Present: Chaoyu, Qi En
Absent: None

## Agenda
Item | Description
--- | ---
Review | Run through past week's progress
Discuss | Backup data source/API for stocks data
Discuss | Plans if tasks cannot be completed in time

## Discussion Items
Item | Decision | Considerations
--- | --- | ---
API routes | Get a list of stocks from backend, correlation matrix for 2 stocks, tests for those routes | Minimum routes required for the full flow of the frontend
Git branching strategy | Git flow, run tests before merging from dev to master | Flow we are all familiar with, good for allowing work on multiple features at once, ensuring no regressions on master branch
Backup data source | Try other APIs, then stale data from database | If one API becomes available, we would still like to try to provide live data by accessing another API. Failing that, we can build an image using the stale data that we have already collected from our the primary API chosen.
Plans if tasks cannot be completed in time | APIs: return mock data so we can begin integration with the frontend for the next stage of development. Unit test CI pipeline: we will drop this feature as automated unit testing can also be performed locally using git hooks. | Optimizing concurrent development, while prioritizing features that contribute towards a minimum viable product. 

## Action Items
Item | By | Due
--- | --- | --- 
Integration with Nasdaq API | Qi En | 04/11/2022
Save data to local database | Qi En | 04/11/2022
Design basic API routes | Henry | 04/11/2022
Convert tests to pytest | Henry | 04/11/2022
Github actions CI pipeline for unit testing | Chaoyu | 04/11/2022
