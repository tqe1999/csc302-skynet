# CSC302 Meeting Minutes - September 25, 2022

# Attendance

Note Taker: Henry (Kuan-Te)
Present: Henry (Kuan-Te), Chaoyu, Qi En
Absent: None

# Agenda

| Meeting Item                                                                  | Description                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Discuss the availability, experience, workload, and goals of each team member | Each member will provide their availability, experience, workload, and what we want to contribute/attain from this project. knowing these information will allow us to create realistic goals and expectations for the project |
| Project data set/data source to use                                           | Each member will provide their idea(s) for which data set to use for the project                                                                                                                                               |
| Tech stack                                                                    | Discuss the tech stack with the factors discussed in the first agenda item kept in mind                                                                                                                                        |
| Timeline                                                                      | Workload distribution, next steps                                                                                                                                                                                              |

# Meeting Items Discussed

### Discuss the availability, experience, workload, and goals of each team member

* Henry: Availability after 4 p.m every day as he is only taking this course. Experience: frontend/backend with JavaScript mainly, but have only used python in academic settings. Have had coop experience in the industry primarily with JavaScript/react. Goal: learn something new, but with familiar technology so as to not spend too much time learning the techstack; to deliver the product on-time.
* Chaoyu: 5 courses, available W R F, experience in webdev, google cloud. Goal: same as Henry.
* Qi En: 5 courses, available tues and thurs. Experience in full stack, focus on backend, machine learning, devops, and infrastructre

### Data source

* General ideas for now, but will elaborate in the next meeting
* Chaoyu suggested the Toronto crime dataset located at the [Toronto Police Service Public Safety Data Portal](https://data.torontopolice.on.ca/). This data is not live, thus more reliable than an API.
* Henry suggested taking soccer or basketball data to predict which team will win next.
* Qi En suggested using financial data: identifying correlations between stock prices, and correlations between stock market and overall. 
**![](https://lh5.googleusercontent.com/g72rzAEF5U3ecubnEimrGvdtJSPY2RLzfZvdIiPV6Pvlz9IAe0-ObBflTdmbm1m9SlkyEGoxDsu3j1fmY6FMQ1OKTJlaUQi-F4otLIBB5Ke8Jfw-bkJDGHrmMu1Xe6eSYlTEER1hPW_fo16LrCXFnHIeGkZG02PgYbf8wzEQ5w8b91uX4iaqGk9yog)**

### Data source

* We all want to use familiar technology as per the goals talked about in the first portion of the meeting.</li><li>All three of us have experience with Python. From our experience using Python, Python has a wide array of data processing libraries, as well as data visualization libraries (for instance, this library for generating graphs called [plotly](https://dash.plotly.com/) ).
* We are also familiar with JS. Henry favors JS more. Qi En has more backend experience.
* Based off the above factors, a preliminary idea for the techstack will be the following:
    * Containerization: Docker, strong adoption rate, strong ecosystem of prebaked images to build upon, highly portable, availability of serverless hosting platforms, lightweight compared to VMs like Vagrant. Team members are familiar with it. Docker-compose, simplest multi-container orchestration tool for our use case of running a handful containers on a single host. Simplify install and setup. Kubernetes too complicated, unnecessary configuration overhead for our purposes
    *  Database we will decide after deciding on data source:
        * SQL
            * Postgres
        * NoSQL
             * MongoDB
             * DynamoDB
             * Firestore
             * Redis
    * Backend (API): Henry only knows express.js. The rest know flask/django. We decided on python to diversify our codebase, as different team members have varying skill levels on frontend and backend. We will decide on the framework in our next meeting after we decide on which database to use.
        * Testing framework: TBD, no decision on framework yet.
    * Backend (data pipeline): Python since the API server will also use python. This simplifies integration.
        * Testing framework: TBD, no decision on framework yet.
    * Code formatter: Black (python), prettier (js) - Industry standard code formatters enforcing code formatting best practices, but configurable to meet our use cases
    * Frontend: JS, see reason for backend (API). React has a strong ecosystem of components, good support (documentation/community discussions). Plus, we want our frontend to have a modern look and feel. This means that the frontend must be dynamic, and not static. Using a framework like React is a natural choice. We decided not to use other frameworks such as Angular since we have less exposure to it. Using React, a framework which we are all familiar with, allows us to save the time it takes towards acquiring a new framework and use that time towards development.
        * Jest (react only): allows testing and mocking

### Preliminary plan

* Milestones (the first milestone only, the rest TBD):
    * Before assignment 1 submission: decide on data source, finalize choices on database, testing, and frameworks.
 * Responsibilities for each milestone:
 * Immediate next actions:
     * Setup repository folders
     * Research about data sources and how to integrate them
     * Monitor assignment 1 due date