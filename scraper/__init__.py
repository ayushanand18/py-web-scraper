"""
Running the Scraper Script
"""
import sqlite3
from main import VergeResponse

DB_NAME = "/workspaces/py-web-scraper/test.db"
RECORDS_OFFSET = 0

try:
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("SELECT * FROM articles ORDER BY id DESC LIMIT 1;")
    last_id = 9
    if last_id:
        RECORDS_OFFSET = last_id + 1
    con.close()
except:
    pass

response = VergeResponse(RECORDS_OFFSET, DB_NAME)

response.fetch_articles()
# response.export_to_csv(".")
response.dump_to_db()
