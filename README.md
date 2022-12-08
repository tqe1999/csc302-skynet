# CSC302 Team Skynet

## Introduction

This project is intended for stock traders who want to visualize how multiple stocks correlate with each other, for the deciding whether to buy, sell, or hold certain stocks.

By leveraging to the [NASDAQ API](https://data.nasdaq.com/tools/api), we are able to access the data of publicly traded U.S stocks which we have used as out dataset.

With this dataset, a correlation matrix may be generated.  This correlation matrix compares at least 2 stocks and shows how they correlate with each other on a scale of -1 to 1.

We've decided to present the dataset this way because we want to present the dataset in an interesting manner.  For example, an uninteresting way this dataset could have been presented is to simply display the stocks in a list, with fields pulled straight from the API (essentially making an inferrior version of stock scanners which already exist).

Our idea is to takes multiple stocks, do some mathematical comparions behind the scenes, and then to funnel it back to the user in a visually rich manner (the matrix).

## User Guide
Run **install-env.sh** to install the environment (Docker), then **build.sh** to build the application, and **test.sh** to run and test the application's API.

After running the application, go to http://localhost:3000/ to open the frontend.  The user will be prompted to add at least 2 stocks.  Click the **"Add Stock +"** button to add a dropdown menu, and select from the list of stocks.

As long as at least 2 stocks have been selected, the application will fetch and display the correlation matrix associated with thos stocks.  This fetching and displaying process is automatic, and any stocks which were de-selected, deleted, or added will trigger this fetching and displaying process.

The correlation matrix will be a **n** by **n** matrix which shows how the **n** stocks selected correlate with each other on a scale of -1 to 1.

## Directories
**Meeting notes** are in [/minutes](https://github.com/tqe1999/csc302-skynet/tree/main/minutes), **documentation** and **roadmap** are in [/documentation](https://github.com/tqe1999/csc302-skynet/tree/main/documentation).

## Undelivered features
Here is a list of our undelivered features.  This is based off our our documented list of features [here](https://github.com/tqe1999/csc302-skynet/blob/main/documentation/features.md).

 - Implement API routes for additional functionalities (stock predictions, etc.).
 - Improve frontend styling, implement custom designs and responsiveness.
   - Frontend should be usable on both web and mobile views.
   
The justification for scraping these features were discussed in our final meeting [documented here](https://github.com/tqe1999/csc302-skynet/blob/main/minutes/meeting-7.md)

For convenience's sake, it will be pasted verbatim here:

**"These features were in our last two milestones (milestones 3 and 4) and can be thought of as "strech goals" conceived of early on in the project. The first feature listed would have taken too long to implement; none of us have a strong background in machine learning so stock predictions is way out of our depths. The second feature, in particular the mobile component of it, was not necessary to have as the project is to be run only on a linux machine.
All in all, the absence of these features did not compromise the minimum viable product; the core features of the product are present and we are happy with what we produced with the time allotted."**


## For assignment 3
The **blameless postmortem for assignment 2** can be found [here](https://github.com/tqe1999/csc302-skynet/blob/main/documentation/blameless-postmortem-2.md). The **presentation materials** can be found [here] (https://github.com/tqe1999/csc302-skynet/blob/main/documentation/Presentation.pdf)