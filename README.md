# py-web-scraper
A Python Web Scraper 

## To Do
+ [ ] Read the headline, get the link of the article, the author, and the date of each of the articles found on "theverge.com"
+ [ ] Store these in a CSV file titled `ddmmyyyy_verge.csv`, with the following header `id, URL, headline, author, date`.
+ [ ] Create an SQLite database to store the same data, and make sure that the id is the primary key
= [ ] Run this script on a cloud service (preferably AWS)
+ [ ] Save the articles (and de-duplicate them) daily on the server in a SQL Database

## Requirements
### `csv` file format
```text
id, url, headline, author, date (YYYY/MM/DD)
```

## Additional Guidelines
+ Adhering to the coding guidelines, and OOP.
+ Writing unit tests for the same.

&copy; Ayush Anand 2023
