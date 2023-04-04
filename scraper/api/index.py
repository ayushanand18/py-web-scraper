"""
Running the Scraper Script
"""
import sqlite3
from flask import Flask
from flask import request
from flask import send_file

from ._main import VergeResponse

app = Flask(__name__)

DB_NAME = "data/database.sqlite"
RECORDS_OFFSET = 0

try:
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    last_id = cur.execute("SELECT * FROM articles ORDER BY id DESC LIMIT 1;").fetchone()
    if last_id is not None:
        RECORDS_OFFSET = last_id[0] + 1
    con.close()
except:
    RECORDS_OFFSET = 0

response = VergeResponse(RECORDS_OFFSET, DB_NAME)

@app.route('/')
def home():
    return 'Running Web Scraper to scrape theverge.com'

@app.route('/fetch_articles')
def fetch_articles():
    """
    Fetch fresh articles from theverge.com as well as tore them into csv file and dump to DB
    """
    try:
        response.fetch_articles()
        response.export_to_csv("data/.")
        response.dump_to_db()
    except:
        return "An exception occurred while running the service."
    return "Successfully Updated Articles"

@app.route('/get_csv')
def get_csv():
    """
    Get the CSV file of specified date
    """
    try:
        date = request.args.get('date')
        return send_file(f"../data/{date}_verge.csv")
    except:
        return "An unexpected exception has occurred."

@app.route("/get_data")
def get_data():
    """
    Get the data fetched so far (limited to top 100 records)
    """
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    results = []
    try:
        for data in cur.execute("SELECT * FROM articles;"):
            results.append(data)
        con.close()
        return results
    except:
        return "No data found."

if __name__ == '__main__':
    app.run()