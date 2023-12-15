import pytest
import requests
from histeventexplorer_pkg.fetch_events import fetch_historical_events

def test_fetch_historical_events_success(monkeypatch):
    sample_data = [
        {'year': '1969', 'event': 'Moon landing'},
        {'year': '1969', 'event': 'Woodstock Music Festival'}
    ]

    def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self):
                pass
            
            def json(self):
                return sample_data

        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_historical_events('dummy_api_key', text='moon landing', year=1969)

    assert result == sample_data

def test_fetch_historical_events_failure(monkeypatch):
    
    def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self):
                raise requests.exceptions.HTTPError("API Error")
            
            def json(self):
                return None

        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_historical_events('dummy_api_key', year=1969)

    assert result is None
