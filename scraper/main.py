"""
Methods to scrape theverge.com for articles
"""
import csv
import sqlite3
from datetime import datetime

import requests
from bs4 import BeautifulSoup

class VergeResponse(object):
    """
    A Verge Articles Response Class

    VergeResponse.FEED_URL: contains the URL to the RSS FEED
    VergeResponse.data: The fetched articles metadata as a Pandas DataFrame Object
    VergeResponse.last_updated: The time at which the content was last updated

    Private Data Members
    VergeResponse.__request_headers: Query Request Headers to avoid being detected as a bot by the URI
        with some user-agent string of a real device.
    VergeResonse.__currCount: current Count of records in the DB
    """
    def __init__(self, offset: int, db_instance: str):
        """
        Initialising the object's required data members
        """
        self.FEED_URL = "https://www.theverge.com/rss/index.xml"
        self.data = None
        self.last_updated = None
        self.offset_records = offset
        self.db_instance = db_instance

        # private data members
        self.__request_header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"}

    def fetch_articles(self) -> None:
        """
        Fetch Articles from The Verge in the form of a list of dictionaries

        :return: None. Sets data member to the results fetched
        """
        response = requests.get(self.FEED_URL, headers = self.__request_header, timeout=300)
        parsed = BeautifulSoup(response.text, features="xml")

        self.last_updated = datetime.strptime(parsed.feed.updated.text, "%Y-%m-%dT%H:%M:%S%z")
        
        results = []
        for entry in parsed.feed.findAll("entry"):
            authors = []
            for author in entry.author.findAll("name"):
                authors.append(author.text)
            
            articleData = {
                "id": self.offset_records,
                "url": entry.id.text,
                "authors": authors,
                "headline": entry.title.text,
                "date": entry.published.text[:10].replace("-", "/"),
            }
            self.offset_records += 1
            results.append(articleData)
        self.data = results
        self.offset_records += results.__len__()
    
    def export_to_csv(self, file_path: str) -> None:
        """
        Export fetched data to a csv file

        :param file_path: [String] The location to save CSV File to. File name will be auto-generated.
        :return: None. Saves the data as CSV file at file_path location.
        """
        if not self.data:
            print("Fetch the data first before dumping into CSV file.")
            return

        file_name = f"{file_path}/{datetime.strftime(self.last_updated, '%d%m%Y')}_verge.csv"
        keys = self.data[0].keys()
        try:
            with open(file_name, 'w', encoding='utf8', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(self.data)
        except:
            print(f"An exception occurred while daving the file {file_name}. Make sure the path exists.")
    
    def dump_to_db(self) -> None:
        """
        Dump fetched responses to a specified .sqlite DB
        """
        if not self.data:
            print("Fetch the data first before dumping into SQLITE DB.")
            return
        
        con = sqlite3.connect(self.db_instance)
        cur = con.cursor()
        try:
            cur.execute("CREATE TABLE articles(id PRIMARY KEY, url, authors, headline, date DATE);")
        except:
            print("Table already present.")
        
        for entry in self.data:
            cur.execute(
                """INSERT INTO articles VALUES (?,?,?,?,?);""",
                (entry["id"], entry["url"], handlestr(entry["authors"]), entry["headline"], entry["date"])
                )
            con.commit()
        con.close()

def handlestr(x: list) -> str:
    """
    A utility function to help desolve python list into space seperated list of strings
    """
    result = ""
    for element in x:
        result += " " + str(element)
    return result