import requests

def fetch_historical_events(api_key, text=None, year=None, month=None, day=None, offset=None):
    """
    Fetch historical events from the API Ninjas Historical Events API.

    Parameters:
    api_key (str): API key for the Historical Events API.
    text (str, optional): Text query to search events by keywords or phrases.
    year (int, optional): 4-digit year to filter events.
    month (int, optional): Integer month (1-12) to filter events.
    day (int, optional): Calendar day (1-31) to filter events.
    offset (int, optional): Offset for pagination.

    Returns:
    list: A list of historical events matching the search criteria.

    Example:
    >>> events = fetch_historical_events('YOUR_API_KEY', text='moon landing', year=1969)
    >>> print(events)
    """
    url = 'https://api.api-ninjas.com/v1/historicalevents'
    headers = {'X-Api-Key': api_key}
    params = {'text': text, 'year': year, 'month': month, 'day': day, 'offset': offset}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        return None





