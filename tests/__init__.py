"""
Tests for VergeResponse Scraper Class
"""
from scraper.api.main import VergeResponse

response = VergeResponse(0, "test.sqlite")

def test_fetch_articles():
    """testing fetching of articles"""
    assert not response.data
    response.fetch_articles()
    assert response.offset_records > 0
