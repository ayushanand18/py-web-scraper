"""
Tests for VergeResponse Scraper Class
"""
from scraper.api._main import VergeResponse
import sqlite3

response = VergeResponse(0, "test.sqlite")

def test_fetch_articles():
    """testing fetching of articles"""
    # at first the data is None
    assert not response.data

    # fetch articles, teh fetched articles are moved into response.data
    response.fetch_articles()
    assert response.data.__len__() > 0

    # dump to sqlite
    response.dump_to_db()

    # make an sql connection
    con = sqlite3.con(response.db_instance)
    cur = con.cur()

    # now we will check if data is redundant or not
    oldRecordCount = cur.execute("SELECT * FROM articles ORDER BY id DESC LIMIT 1;").fetchone()

    # fetch data again
    response.fetch_articles()

    # dump to db again, although this gives no exception but 
    # data must not get changed, as we perform de-duplication check
    # while insertion
    response.dump_to_db()
    newRecordCount = cur.execute("SELECT * FROM articles ORDER BY id DESC LIMIT 1;").fetchone()
    assert oldRecordCount == newRecordCount