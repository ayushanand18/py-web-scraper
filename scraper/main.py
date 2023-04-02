import pandas as pd

class VergeResponse(object):
    """
    A Verge Articles Response Class

    VergeResponse.FEED_URL: contains the URL to the RSS FEED
    VergeResponse.data: The fetched articles metadata as a Pandas DataFrame Object
    """
    def __init__(self):
        """
        Initialising the object's required data members
        """
        self.FEED_URL = "https://www.theverge.com/rss/index.xml"
        self.data = None

    def fetch_articles(self):
        pass