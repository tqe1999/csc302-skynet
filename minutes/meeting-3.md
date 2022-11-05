# CSC302 Meeting Minutes - October 18, 2022

## Attendance

Taken by: Chaoyu
Present: Henry (Kuan-Te), Qi En
Absent: None

## Agenda

| Meeting Item Type | Meeting Item                 | Description                                                                              |
| ----------------- | ---------------------------- | ---------------------------------------------------------------------------------------- |
| Review            | Weekly review                | Discuss blockers and progress since the last meeting                                     |
| Decide            | Decide financial data source | We've decided on which type of dataset to use, now it's time to decide on a specific API |
| Decide            | Assign work                  | Assign work to each group member for this assignment period                              |

## Meeting Items Discussed

### [Review] Weekly review

- All members have done some preliminary research on which API to use

### [Decide] Dataset

- By way of a rigorous discussion, the API we will use will be the [NASAQ API](https://data.nasdaq.com/publishers/QDL)
- This API has several advantages:
  - It should have good reliability and uptime due to it being supported by a reputable company (NASDAQ)
  - The API may be accessed without a secret key
    - This eliminates secret mangament, which was one of our concerns
  - The [Quandl library for Python](https://github.com/quandl/quandl-python), which is tailored for this API, makes the data easily query-able. This can’t be said about other APIs
  - There are many alternative stocks API choices. However, our project has limited scope and performance requirements, so there isn’t much need to choose carefully besides making sure that our choice would be reliable
    - In addition, the API provides sufficient fields for us to do our calculations

### [Decide] Assign work

| Item                                                                | Assigned to | Due              |
| ------------------------------------------------------------------- | ----------- | ---------------- |
| Integration with Nasdaq API and caching responses in local database | Qi En       | November 4, 2022 |
| Implement API routes                                                | Henry       | November 4, 2022 |
| Convert tests to PyTest, implement API tests                        | Henry       | November 4, 2022 |
| Implement Github Actions CI pipeline for automatic running of tests | Chaoyu      | November 4, 2022 |
| Make detailed plans and development tasks                           | Everybody   | November 4, 2022 |
