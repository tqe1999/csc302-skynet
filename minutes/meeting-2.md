# CSC302 Meeting Minutes - October 1, 2022

## Attendance

Taken by: Qi En 
Present: Henry (Kuan-Te), Chaoyu
Absent: None

## Agenda

| Meeting Item Type | Meeting Item                      | Description                                                                 |
| ----------------- | --------------------------------- | --------------------------------------------------------------------------- |
| Review            | Weekly review                     | Discuss blockers and progress since the last meeting                        |
| Decide            | Dataset                           | We had three candidates for datasets be and it will be decided this meeting |
| Decide            | System requirement                | Need to decide the operating system(s) our application will support         |
| Discuss           | Implementation details            | Discuss how the software we decided on will all fit together                |
| Decide            | Workload distribution, next steps | Distribute any work which needs to be done                                  |

## Meeting Items Discussed

### [Review] Weekly review

* All 3 members had no blockers
* Signficant progress has been made in the realm of researching the tech stack.  This progress will be talked about later under the **Implementation details** meeting item

### [Decide] Dataset

* All 3 members brought up the pros & cons of their dataset after which, a vote was held to decide which dataset to go with
* Chaoyu's dataset was the crimes statistics located at [Toronto Police Service Public Safety Data Portal](https://data.torontopolice.on.ca/).
  * Pros:
    * Comprehensive dataset which organizes crime by crime type, dates, location (even down to the neighbourhood) and many more.
      * Definitly a lot of potential here
    * Can be downloaded thus accecible offline; great for our website reliability
  * Cons:
    * The Toronto Police already has a website which is very modern and responsive.  It features various pictorial ways to interpret the data
      * It will be challenging to improve upon this or come up with an idea which isn't already done prior
  * Henry's dataset was basketball team statics.  He linked to [this rapidapi page](https://rapidapi.com/collection/basketball) which have many free public APIs to choose from
  * Pros:
    * A lot of free public APIs
  * Cons:
    * Henry's idea is hard to implement
      * He wants to use exisiting basketball data to predict who the winner will be for the next game.  We don't know how we can reliabily predict the next winner as it involves some deep understaning of statistics
    * The team struggled to come up with an interesting idea, other than the aformentioned idea which is hard to implement, for the basketball dataset
  * Qi En's dataset are stock data
    * Pros:
        * The idea is the most unique of the 3.  Using the stock data, we can pick **n** number of stocks, and  see how tightly each stock tracks with each other
            * This may be presented as a **n** by **n** grid, like the one below ![Drag Racing](https://camo.githubusercontent.com/90817b50c56628f04ff85c47fe26b0baf71e7a0971b2b8279edffa3cc9d20094/68747470733a2f2f6c68352e676f6f676c6575736572636f6e74656e742e636f6d2f673732727a414546355533656375626e45696d72477664744a53505932524c7a665a7664496950563650766c7a39494165302d4f6242666c54646d626d316d39536c6b7945476f78447375336a31666d5936464d51314f4b544a6c615551692d46346f744c494242354b65384a66772d626b4a444748726d4d75315865366553596c54454552316850575f666f31364c724358466e484965476b5a473032506759626638777a4551357738623931755834696171476b39796f67)
            * The proposed imlementation seems straightforward, as the **matplotlib** library for **Python** is capable of creating a picture like the above
        * Cons:
            * Many APIs for stocks are private, and requires an API key.  We don't have experience with packaing API keys within our deliverables and could prove to be a challenge
            * Henry and Chaoyu is not as financial-savvy as Qi En, so Qi En might need to explain certain concepts
* All three members voted in favor of using Qi En's dataset

### [Decide] System requirement

* Our application must function on a modern linux system
* This is a pretty broad definition, so some reasonable assumptions must be made
    * This system has access to the unix shell, and shell files may be executed
    * This system needs to have programs pre-loaded onto it which allows it to retrieve files on the internet, through various protocals such as HTTP and HTTPS
        * The most popular of these are **wget** and **curl**
* Thus, our program should work with linux systems with access to the unix shell and has one of **wget** or **curl**

### [Discuss] Implementation details

* Team members disucessed the teck stack, and the justifications of using the various technologies.  Much of it is a re-hash of what is already on [this document](https://github.com/tqe1999/csc302-skynet/blob/main/documentation/tech-stack.md) so for the sake of brevity, please refer to that document

### [Decide] Workload distribution, next steps

| Item                              | Assigned to   | Due             |
| --------------------------------- | ------------- | --------------- |
| Documentation (packaging, CI/CD)  | Qi En         | October 6, 2022 |
| Documentation (frontend)          | Chaoyu        | October 6, 2022 |
| Documentation (backend, database) | Henry         | October 6, 2022 |
| Toy application                   | Qi En         | October 6, 2022 |
| Roadmap                           | Chaoyu, Henry | October 6, 2022 |