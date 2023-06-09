# Development Notes
> This document details the development experience of the script including the steps while setting up and the challenges faced during the process.

## Poetry Package
+ The python script is created as a `poetry` package so that it is easier to manage dependencies and environment.
+ The script fetches all the articles on theverge.com and dumps them into a .sqlite DB.
    + For fetching all news articles we will use the RSS Feed by The Verge (https://www.theverge.com/rss/index.xml) which is updated at `20:10:38 GMT -04:00` everyday. So we will aim to run this cron job around this time each day to get the updated feed.
    + One of the most obvious methods of fetching this data and dumping it into a csv file could be using the `pandas.read_xml()` function. This would allow us to fetch the data directly into a DataFrame and then easily dumping it into a csv file. However, we chose using `bs4` package to parse the `xml` doc and constructed the `result` object ourselves. So, that we do not have to work hard in cleaning the responses and aligning the row headers with the data we have. 
    + Also, dumping from a python object (particularly a list of dictionaries) to a CSV file is pretty easy. We can just open the file at the specified path and use the built-in csv library to our task.
+ Deploying this service on AWS is a good choice but I hit wall on this because setting up an instance on AWS requires a valid payment method (which I lack, and students discounts are also gone).
    + So, I deployed this service on Vercel as a cron-job which would run at 22:00 UTC -04:00 (i.e. 07:30 UTC +05:30) everyday.
    + Since SQLite is a serverless DB written in C, it essentially needs no server to be setup. It is stored as as a disk file in binary format.
+ While using the RSS Feed URL provided by Verge, it worked fine on till 4th April. However, on 5th April the domain stareted to redirect to an AWS S3 URL, and access curtailed. So, we created I switched the RSS Feed URL. Finally, the service deployed started working again.