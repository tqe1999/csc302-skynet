# CSC302 Meeting Minutes - 18/10/2022

## Attendance
Taken by: Chaoyu
Present: Henry (Kuan-Te), Qi En
Absent: None

## Agenda
Item | Description
--- | ---
Review | Run through past week's progress
Decide | Choose financial dataset
Discuss | Implementation details
Decide | Workload distribution, next steps

## Discussion Items
Item | Decision | Considerations
--- | --- | ---
Financial dataset | Decided on Nasdaq data link, via tha Quandl package. | Nasdaq is a reputable provider of financial data, and is a large company which is less likely to become defunct or have its APIs go down. It allows access to the API without requiring an API key, removing the need to handle secret management and simplifying the development process. In comparison, other APIs either require an API key to make requests at all, or severely rate limit requests. Nasdaq also provides a python package, Quandl, that simplifies access to that dataset, as opposed to many other sources which require making raw http requests.
API key | Prompt user for API key if required | Chaoyu raised concerns about including the API key if any with the docker image, since this poses security issues and would result in the application being rate limited in API requests across all its instantiations. As such, if an API key is required, we would prompt the user for the API key while building the application. This would typically be done via creating an account directly with the data provider, but we would provide it in the github repo as well for the tester's convenience.

## Action Items
Item | By | Due
--- | --- | --- 
Integration with Nasdaq API | Qi En | 04/11/2022
Save data to local database | Qi En | 04/11/2022
Design basic API routes | Henry | 04/11/2022
Convert tests to pytest | Henry | 04/11/2022
Github actions CI pipeline for unit testing | Chaoyu | 04/11/2022
