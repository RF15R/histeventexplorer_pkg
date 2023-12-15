import pytest
from histeventexplorer_pkg.event_trends import (
    analyze_event_types_over_time,
    analyze_event_density,
    analyze_event_patterns,
)


@pytest.fixture
def mock_fetch_historical_events(monkeypatch):
    def mock_fetch_events(api_key, year):
        if year == 1800:
            return [{'year': '1800', 'event': 'A big war happened'}]  # 'war' event in 1800
        elif year == 1801:
            return [{'year': '1801', 'event': 'An amazing invention was made'}]  # 'invention' event in 1801
        return []  # No events in 1802
    
    monkeypatch.setattr(
        'histeventexplorer_pkg.event_trends.fetch_historical_events', mock_fetch_events
    )


def test_analyze_event_types_over_time(mock_fetch_historical_events):
    api_key = 'fake_api_key'
    start_year = 1800
    end_year = 1801
    event_types = ['war', 'invention']
    expected_result = {'war': 1, 'invention': 1}

    result = analyze_event_types_over_time(api_key, start_year, end_year, event_types)
    assert result == expected_result

    
def test_analyze_event_density(mock_fetch_historical_events):
    api_key = 'fake_api_key'
    start_year = 1800
    end_year = 1802
    interval = 1
    event_types = ['war', 'invention']

    expected_result = {
        '1800-1800': {'war': 1, 'invention': 0},
        '1801-1801': {'war': 0, 'invention': 1},
        '1802-1802': {'war': 0, 'invention': 0}
    }

    result = analyze_event_density(api_key, start_year, end_year, interval, event_types)
    
    
    print(f"Expected: {expected_result}")
    print(f"Result: {result}")

    assert result == expected_result

def test_analyze_event_patterns(mock_fetch_historical_events):
    api_key = 'fake_api_key'
    start_year = 1800
    end_year = 1801
    keyword = 'war'
    expected_result = {1800: 1, 1801: 0}
    
    result = analyze_event_patterns(api_key, start_year, end_year, keyword)
    assert result == expected_result
