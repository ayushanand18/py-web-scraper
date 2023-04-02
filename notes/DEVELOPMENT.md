# Development Notes
> This document details the development experience of the script including the steps while setting up and the challenges faced during the process.

## Poetry Package
+ The python script is created as a `poetry` package so that it is easier to manage dependencies and environment.
+ The script fetches all the articles on theverge.com and dumps them into a .sqlite DB.
    + For fetching all news articles we will use the RSS Feed by The Verge (https://www.theverge.com/rss/index.xml) which is updated at `20:10:38 GMT -04:00` everyday. So we will aim to run this cron job around this time each day to get the updated feed.