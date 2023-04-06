# Method 
> This document details the algorithm (method) used to accomplish the task, and observations why this is a better method among other possible solutions (that came to my mind).

## Introduction
We had to create a python based web scraper which would fetch articles from [theverge.com](theverge.com). We deployed the service on Vercel, which helped us in two ways:
1. The service could be run as a cron-job everyday.
2. The fetched data can also be viewed easily with a web browser without logging into the web server or instance.

Overall, the motivation behind the chosen method has been widely discussed in the [Method](#chosen-method) section.

## Files included
This repository contains all the code and data files required to create this web scraper.
Overall, the directory structure is as follows:

```text
|--- notes/ # all the notes have been discussed here
|--- scraper/ # all the necessary files for the script to work, this folder is deployed directly
    |--- api/
        |--- index.py # the default flask app file
        |--- _main.py # the utility python file (containing all the class definitions)
    |--- data/
        |--- *_verge.csv # the dumped csv files with fetched data
        |--- database.sqlite # the SQLite database file
    |--- .gitignore
    |--- requirements.txt
    |--- vercel.json # the configuration file for Vercel
|--- tests/ # unit tests
    |--- __init__.py # all simple unit tests written in this file
|--- .gitignore
|--- poetry.lock # this project usespotery to manage dependencies
|--- pyproject.toml # all the project information and dependencies
|--- README.md
```

## API Description
```json
{
    "base_url" = "https://scraper-theta.vercel.app/",
    "endpoints": {
        "/fetch_articles" : "Run articles fetch and dumping to csv, DB.",
        "/get_data": "Get all records from (limitted to top 100 records to save bandwidth).",
        "/get_csv?date=DDMMYYYY": "Return the CSV file for specified date.",
    },
}
```

## Possible Solutions
1. One of the possible methods to implement a web scraper that could fetch articles from [theverge.com](theverge.com) using the RSS Feed that it provides. The RSS feed resets every day at `20:10:38 GMT -04:00` so we can run this script as a cron job around that time each day.

2. Another method to get instant feeds is by scraping the website directly. But it would be very complex to fetch articles from the website directly due to difference in DOM design for featured articles and non-featured articles.

## Chosen Method
We chose Method 1 (to directly ping to the RSS Feed) not because the method was easier, but because it provided cleaner and quality data. 

### Algorithm

#### Fetching Articles
1. Get the latest RSS Feed of [theverge.com](https://www.theverge.com/rss/index.xml) by a simple GET request.
2. Parse the response using `lxml` package.
3. Create a list of dictionaries and feed parsed data into it.
4. Return this list of results.

#### Dumping to DB
1. Fetch all the data of the instantiated object.
2. For each record, check if it is already present in the database.
3. If not present, insert the values into database.

## Discussion and Conclusion
Overall, the method employed to accomplish the idea was pretty much accurate. But it can improved further by doing the following changes:
1. Scraping the website directly so that realtime articles are fetched. But this would imply less clean data and demands more efforts into a collecting quality data.

Thanks!