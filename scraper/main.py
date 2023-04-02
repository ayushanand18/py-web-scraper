import bs4
import pandas as pd
import requests

class VergeResponse(object):
    """
    A Verge Articles Response Class

    VergeResponse.FEED_URL: contains the URL to the RSS FEED
    VergeResponse.data: The fetched articles metadata as a Pandas DataFrame Object

    Private Data Members
    VergeResponse.__request_headers: Query Request Headers to avoid being detected as a bot by the URI
        with some user-agent string of a real device.
    """
    def __init__(self: VergeResponse) -> VergeResponse:
        """
        Initialising the object's required data members
        """
        self.FEED_URL = "https://www.theverge.com/rss/index.xml"
        self.data = None

        # private data members
        self.__request_header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"}

    def fetch_articles(self: VergeResponse):
        """
        Fetch Articles from The Verge in the form of a pandas DataFrame

        :return: A Pandas DataFrame Object
        """
        pass
    
    def export_to_csv(self: VergeResponse, file_path: str) -> None:
        """
        Export fetched data to a csv file

        :param file_path: [String] The location to save CSV File to. File name will be auto-generated.
        :return: None. Saves the data as CSV file at file_path location.
        """
        pass
    
    def dump_to_db(self) -> None:
        """
        Dump fetched responses to a .sqlite DB
        """
        pass