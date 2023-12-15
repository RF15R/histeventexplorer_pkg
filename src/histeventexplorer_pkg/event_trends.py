import requests
from collections import Counter
import matplotlib.pyplot as plt

def analyze_event_types_over_time(api_key, start_year, end_year, event_types):
    """
    Analyze the frequency of different types of historical events over a specified time period.

    Parameters:
    api_key (str): API key for the Historical Events API.
    start_year (int): Starting year of the period for analysis.
    end_year (int): Ending year of the period for analysis.
    event_types (list of str): List of event types to analyze (e.g., 'war', 'invention').

    Returns:
    dict: A dictionary with event types as keys and their frequency as values.

    Example:
    >>> event_counts = analyze_event_types_over_time('YOUR_API_KEY', 1800, 1900, ['war', 'invention'])
    >>> print(event_counts)
    """
    event_counts = {event_type: 0 for event_type in event_types}
    
    for year in range(start_year, end_year + 1):
        events = fetch_historical_events(api_key, year)
        if events:
            for event in events:
                event_description = event.get('event', '').lower()
                for event_type in event_types:
                    if event_type in event_description:
                        event_counts[event_type] += 1

    # Optional: Plotting the results
    plt.bar(event_counts.keys(), event_counts.values())
    plt.xlabel('Event Types')
    plt.ylabel('Frequency')
    plt.title(f'Frequency of Event Types from {start_year} to {end_year}')
    plt.show()

    return event_counts


def fetch_historical_events(api_key, year):
    """
    Fetch historical events for a specific year.
    """
    url = 'https://api.api-ninjas.com/v1/historicalevents'
    headers = {'X-Api-Key': api_key}
    params = {'year': year}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        return None


def analyze_event_patterns(api_key, start_year, end_year, keyword):
    """
    Analyze the pattern of occurrences of a specific keyword in historical events over a specified time period.

    Parameters:
    api_key (str): API key for the Historical Events API.
    start_year (int): Starting year of the period for analysis.
    end_year (int): Ending year of the period for analysis.
    keyword (str): The keyword to search for in event descriptions.

    Returns:
    dict: A dictionary with years as keys and the count of keyword occurrences as values.

    Example:
    >>> pattern = analyze_event_patterns('YOUR_API_KEY', 1800, 1900, 'revolution')
    >>> print(pattern)
    """
    keyword_counts = {year: 0 for year in range(start_year, end_year + 1)}
    
    for year in range(start_year, end_year + 1):
        events = fetch_historical_events(api_key, year)
        if events:
            for event in events:
                if keyword.lower() in event.get('event', '').lower():
                    keyword_counts[year] += 1

    # Optional: Plotting the results
    plt.plot(list(keyword_counts.keys()), list(keyword_counts.values()))
    plt.xlabel('Year')
    plt.ylabel('Number of Occurrences')
    plt.title(f"Occurrences of '{keyword}' in Historical Events from {start_year} to {end_year}")
    plt.show()

    return keyword_counts



def analyze_event_density(api_key, start_year, end_year, interval):
    """
    Analyze the density of historical events over specified time intervals.

    Parameters:
    api_key (str): API key for the Historical Events API.
    start_year (int): Starting year of the period for analysis.
    end_year (int): Ending year of the period for analysis.
    interval (int): The time interval in years for density calculation (e.g., 10 for decades).

    Returns:
    dict: A dictionary with time intervals as keys and the number of events as values.

    Example:
    >>> density = analyze_event_density('YOUR_API_KEY', 1800, 1900, 10)
    >>> print(density)
    """
    event_density = {}
    for period_start in range(start_year, end_year, interval):
        period_end = period_start + interval
        event_count = 0
        for year in range(period_start, period_end):
            events = fetch_historical_events(api_key, year)
            if events:
                event_count += len(events)
        event_density[f"{period_start}-{period_end - 1}"] = event_count

    # Optional: Plotting the results
    plt.bar(event_density.keys(), event_density.values())
    plt.xlabel('Time Interval')
    plt.ylabel('Number of Events')
    plt.title(f"Event Density from {start_year} to {end_year}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return event_density


def analyze_event_density(api_key, start_year, end_year, interval, event_types):
    """
    Analyze the qualitative density of historical events over specified time intervals, 
    categorized by event types.

    Parameters:
    api_key (str): API key for the Historical Events API.
    start_year (int): Starting year of the period for analysis.
    end_year (int): Ending year of the period for analysis.
    interval (int): The time interval in years for density calculation (e.g., 10 for decades).
    event_types (list of str): List of event types to categorize (e.g., 'war', 'invention').

    Returns:
    dict: A dictionary with time intervals as keys and dictionaries of event type counts as values.

    Example:
    >>> api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    >>> start_year = 1800
    >>> end_year = 1900
    >>> interval = 10
    >>> event_types = ['war', 'invention', 'discovery']
    >>> event_density = analyze_event_density(api_key, start_year, end_year, interval, event_types)
    >>> for period, counts in event_density.items():
    ...     print(f"{period}: {counts}")
    1800-1809: {'war': 2, 'invention': 5, 'discovery': 1}
    1810-1819: {'war': 3, 'invention': 2, 'discovery': 0}
    ... # and so on for each interval
    """
    event_density = {}

    for period_start in range(start_year, end_year + 1, interval):
        period_label = f"{period_start}-{period_start + interval - 1}"
        event_density[period_label] = {event_type: 0 for event_type in event_types}

    # Iterate over each interval
    for period_start in range(start_year, end_year, interval):
        period_end = period_start + interval
        for year in range(period_start, period_end):
            events = fetch_historical_events(api_key, year)
            if events:
                for event in events:
                    event_description = event.get('event', '').lower()
                    for event_type in event_types:
                        if event_type in event_description:
                            event_density[f"{period_start}-{period_end - 1}"][event_type] += 1

    return event_density
