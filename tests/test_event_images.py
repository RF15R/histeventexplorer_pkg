import pytest
from unittest.mock import Mock
from histeventexplorer_pkg.event_image_fetcher import fetch_historical_events, fetch_images_with_serpapi, fetch_events_and_images

historical_events_data = [
    {'year': '1969', 'event': 'Moon landing'},
    {'year': '1969', 'event': 'Woodstock Music Festival'}
]

image_search_data = {
    'images_results': [
        {'thumbnail': 'http://example.com/moon.jpg'},
        {'thumbnail': 'http://example.com/woodstock.jpg'}
    ]
}

@pytest.fixture
def mock_requests_get(monkeypatch):
    
    def mock_get(url, headers=None, params=None):
        if 'api-ninjas.com' in url:
            return Mock(status_code=200, json=lambda: historical_events_data)
        elif 'serpapi.com' in url:
            return Mock(status_code=200, json=lambda: image_search_data)
        else:
            raise ValueError('Unrecognized URL')

    monkeypatch.setattr('requests.get', mock_get)

def test_fetch_events_and_images_success(mock_requests_get):

    api_key_events = 'dummy_api_key_events'
    api_key_images = 'dummy_api_key_images'
    year = 1969

    fetch_events_and_images(api_key_events, api_key_images, year)

   
def test_fetch_events_no_results(mock_requests_get):

    api_key_events = 'dummy_api_key_events'
    api_key_images = 'dummy_api_key_images'
    year = 1900

    historical_events_data.clear()

    fetch_events_and_images(api_key_events, api_key_images, year)

pytest.main()
