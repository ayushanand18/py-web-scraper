# Method 
> This document details the algorithm (method) used to accomplish the task, and observations why this is a better method among other possible solutions (that came to my mind).

## Introduction

## Files included

## Possible Solutions
1. One of the possible methods to implement a web scraper that could fetch articles from [theverge.com](theverge.com) using the RSS Feed that it provides. The RSS feed resets every day at `20:10:38 GMT -04:00` so we can run this script as a cron job around that time each day.

2. Another method to get instant feeds is by scraping the website directly. But it would be very complex to fetch articles from the website directly due to difference in DOM design for featured articles and non-featured articles.

## Chosen Method

### Algorithm
1. Get the latest RSS Feed of [theverge.com](https://www.theverge.com/rss/index.xml) by a simple GET request.
2. Parse the response using `lxml` package.

## Discussion and Conclusion

Thanks!