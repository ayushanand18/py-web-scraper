"""
Running the Scraper Script
"""
from .main import VergeResponse

response = VergeResponse()

response.fetch_articles(0)
response.export_to_csv(".")
