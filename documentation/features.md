# Preliminary explanation
During assignment 1, our team has already created a project roadmap which can be found [here](https://github.com/tqe1999/csc302-skynet/blob/main/documentation/roadmap.md).  It was produced with much thought and much discussion as shown in our meeting notes.  Therefore, we feel that it makes sense to piggy-back off of this document.  The roadmap is broken up into milestones, and each milestone corresponds with an assignment (milestone 1 is to be completed by assignment 2 due date, and milestone 2 is to be completed by assignment 3 due date etc).

Every feature in each milestone has a higher priority than the milestone which proceeds it.  This is because the latter milestones have features which depend on features in earlier milestones. We also prioritize features that are more essential to the minimum viable product. For example, components involving acquiring and presenting key financial data are more important than the look and feel of the frontend.

Finally, we tried our best to make sure every feature within each milestone has equal priority.  This is because we figured that it is best that a task which depends on another task shouldn’t be in the same milestone.  This way, each member can work towards a milestone independently instead of waiting for a high-priority task to be completed before a lower-priority dependent task may proceed.

**This document is still a work in progress and will be updated as progress is made.**

# Milestone 1 (07/10/2022) (In progress)
1. Many stock market APIs/data sources exist, we need to decide on a specific service that we will use for the project.
    * This will be completed when we vote on which service to use
        * **This has been completed in the second meeting**
2. Implement data ingestion/formatting pipeline. The difficulty of this task will depend on the specifications of the stock market API/data source.
	* This will be completed when these two sub-tasks are finished:
		* Create a process to pull data from the NASDAQ API
		* Store the data into the database in a usable form
3. Implement data pipeline execution schedule (manual or automatic), if needed.
    * This will be completed when a process exists which allows feature 2 to be executed with a single manually or automatically executed script
4. Implement unit tests for data pipeline, if needed.
	* This will be completed when the data pipeline is test for the following in pytest:
		* Check if the API is querying the correct data
		* Check if the process is storing to the database in a usable form:
			* Each entry must have a stock name
			* Each entry must have a stock price
			* Each entry must have a date/time stamp
5. Add basic backend routes for testing and debugging purposes.
	* This will be completed if two API routes are implemented:
		* One API route for getting a list of stocks
		* One API route for getting a picture of a correlation graph, based on 2 stocks
		* **These have been completed**
	*In addition, the first API needs to tested for the following in pytest:
		* Check if the API is online for a valid query (status code 200)
		* Check if the API returns a list of stocks for a valid query
		* **These have been completed**
	*In addition, the second API needs to be tested for the following  in pytest:
		* Check if the API is online for a valid query (status code 200)
		* Check if the API returns a picture for a valid query
		* Check if the API throws an error gracefully for an invalid query
		* **These have been completed**

## Responsibilities
- Chaoyu: explore stock market APIs, implement data pipeline and backend.
- Henry: explore stock market APIs, set up test/debug backend routes.
- Qi En: explore stock market APIs, implement data pipeline and backend.