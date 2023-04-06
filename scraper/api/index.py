"""
Running the Scraper Script
"""
import sqlite3
from flask import Flask
from flask import request
from flask import send_file
from flask import jsonify

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
    res = {
        "message":"Running Web Scraper to scrape theverge.com",
        "endpoints": {
            "/fetch_articles" : "Run articles fetch and dumping to csv, DB.",
            "/get_data": "Get all records from (limitted to top 100 records to save bandwidth).",
            "/get_csv?date=DDMMYYYY": "Return the CSV file for specified date.",
        },
    }
    return jsonify(res)

@app.route('/fetch_articles')
def fetch_articles():
    """
    Fetch fresh articles from theverge.com as well as tore them into csv file and dump to DB
    """
    res = {
        "status" : "",
        "message" : "",
    }
    try:
        response.fetch_articles()
        response.export_to_csv("data/.")
        response.dump_to_db()
    except:
        res["status"] = "error"
        res["message"] = "An exception occurred while running the service."
        return jsonify(res)
    
    res["status"] = "success"
    res["message"] = "Successfully Updated Articles."
    return jsonify(res)

@app.route('/get_csv')
def get_csv():
    """
    Get the CSV file of specified date
    """
    try:
        date = request.args.get('date')
        return send_file(f"../data/{date}_verge.csv")
    except:
        res = {
            "status" : "error",
            "message" : "An unexpected exception has occurred.",
        }
        return jsonify(res)

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
        res = {
            "total" : len(results),
            "records" : results,
        }
        return jsonify(res)
    except:
        res = {
            "total" : 0,
            "records" : [],
        }
        return jsonify(res)

if __name__ == '__main__':
    app.run()