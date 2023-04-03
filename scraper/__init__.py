"""
Running the Scraper Script
"""
from main import VergeResponse

response = VergeResponse(0, "test.db")

response.fetch_articles()
# response.export_to_csv(".")
response.dump_to_db()

