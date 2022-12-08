# Preliminary explanation
During assignment 1, our team has already created a project roadmap which can be found [here](https://github.com/tqe1999/csc302-skynet/blob/main/documentation/roadmap.md).  It was produced with much thought and much discussion as shown in our meeting notes.  Therefore, we feel that it makes sense to piggy-back off of this document.  The roadmap is broken up into milestones, and each milestone corresponds with an assignment (milestone 1 is to be completed by assignment 1 due date, and milestone 2 is to be completed by assignment 2 due date etc).

Every feature in each milestone has a higher priority than the milestone which proceeds it.  This is because the latter milestones have features which depend on features in earlier milestones. We also prioritize features that are more essential to the minimum viable product. For example, components involving acquiring and presenting key financial data are more important than the look and feel of the frontend.

Finally, we tried our best to make sure every feature within each milestone has equal priority.  This is because we figured that it is best that a task which depends on another task shouldn’t be in the same milestone.  This way, each member can work towards a milestone independently instead of waiting for a high-priority task to be completed before a lower-priority dependent task may proceed.

# Milestone 1 (Starts 07/10/2022) (Completed)
**In this milestone, we are looking to build the fundamental components for the project.  Before we start doing any calculations and generating any pictures, we need the data.  Thus, this milestone focuses on getting the data in a usable format from the API into our database.  Of course, tests need to accompany these processes, and are a part of this milestone too.  Finally, the API which the frontend will query from will be a part of this milestone too, as that component can be developed independently from the database or the frontend (this allows for clever use of our time as it reduces blockers from dependent components not yet developed).  What constitutes success in this milestone is if all our features below are implemented.**

1. Many stock market APIs/data sources exist, we need to decide on a specific service that we will use for the project.
    * This will be completed when we vote on which service to use
    * **This has been completed in the third meeting, the NASDAQ API was selected through vote**
2. Implement data ingestion/formatting pipeline. The difficulty of this task will depend on the specifications of the stock market API/data source.
	* This will be completed when these two sub-tasks are finished:
		* Create a process to pull data from the NASDAQ API
		* Store the data into the database in a usable form
		* **This has been completed during assigment 3**
3. Implement data pipeline execution schedule (manual or automatic), if needed.
    * This will be completed when a process exists which allows feature 2 to be executed with a single manually or automatically executed script
    * **This has been completed during assigment 3**
4. Implement unit tests for data pipeline, if needed.
	* This will be completed when the data pipeline is test for the following in pytest:
		* Check if the API is querying the correct data
		* Check if the process is storing to the database in a usable form:
			* Each entry must have a stock name
			* Each entry must have a stock price
			* Each entry must have a date/time stamp
			* **This has been completed during assigment 3**
5. Add basic backend routes for testing and debugging purposes.
	* This will be completed if two API routes are implemented:
		* One API route for getting a list of stocks
		* One API route for getting a picture of a correlation graph, based on 2 stocks
		* **These have been completed during assigment 2**
	* In addition, the first API needs to tested for the following in pytest:
		* Check if the API is online for a valid query (status code 200)
		* Check if the API returns a list of stocks for a valid query
		* **These have been completed during assigment 2**
	* In addition, the second API needs to be tested for the following  in pytest:
		* Check if the API is online for a valid query (status code 200)
		* Check if the API returns a picture for a valid query
		* Check if the API throws an error gracefully for an invalid query
		* **These have been completed during assigment 2**
## Responsibilities for milestone 1
- Chaoyu: features 1, 2, 3, 4
- Henry: features 1, 5
- Qi En: features 1, 2, 3, 4

# Milestone 2 (Starts 06/11/2022)
1. Set up a database and schema so that ingested data can be stored on the server side.
 * Determine data required for core functionalities
 * Determine database schema based on data source and data required
 * Implement database schema
 * **This has been completed during assigment 3**
2. Implement API routes related to core functionalities (computing stock trends, generating graphs).
 * Endpoint providing list of stocks for which data is available
 * Endpoint providing computed correlation matrix between stocks
 * **This has been completed during assigment 3**

3. Implement basic frontend for core functionalities, this only needs to be a basic UI (no styling, responsiveness, etc.).
    - List view for the list of stocks
    - Selectors for choosing stocks to include in graphs
    - Implement data fetching (stocks list, graphs)
    - Display graphs in image views
    * **This has been completed during assigment 3**
    
4. Implement auto testing pipeline
    - Set up Github Actions config file to run unit tests for all branches
    * **This has been completed during assigment 2**

## Responsibilities for milestone 2
- Chaoyu: frontend, integration, unit tests.
- Henry: backend, integration.
- Qi En: backend, database.

# Milestone 3 (Starts 20/11/22)
1. Implement API routes for additional functionalities (stock predictions, etc.).
 * **This feature has been scraped**
2. Implement frontend for additional functionalities, including UI and data fetching.
    - Able to search and filter stocks of interest
    * **This was completed during assignment 3**
3. Implement unit tests.
    - Frontend tests
    - Backend tests
    * **This was completed during assignment 3**

## Responsibilities for milestone 3
- Chaoyu: frontend, backend, integration.
- Henry: frontend, unit tests.
- Qi En: backend, integration.

# Milestone 4 (Starts 04/12/22)
1. Improve frontend styling, implement custom designs and responsiveness.
    - Frontend should be usable on both web and mobile views
    * **This feature has been scraped**

## Responsibilities for milestone 4
* All team members will work on frontend improvements.


