import requests

def fetch_historical_events(api_key, year, month=None, day=None):
    """
    Fetch historical events from the API Ninjas Historical Events API.
    """
    url = 'https://api.api-ninjas.com/v1/historicalevents'
    headers = {'X-Api-Key': api_key}
    params = {'year': year, 'month': month, 'day': day}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical events: {e}")
        return []
    

def fetch_images_with_serpapi(query, api_key, num_images=1):
    """
    Fetch images related to a query using the SERP API.
    """
    url = 'https://serpapi.com/search'
    params = {
        'q': query,
        'engine': 'google_images',
        'api_key': api_key,
        'num': num_images
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return [img['thumbnail'] for img in data.get('images_results', [])][:num_images]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching images: {e}")
        return []
    
def fetch_events_and_images(api_key_events, api_key_images, year, month=None, day=None, num_images=1):
    """
    Fetch historical events and their related images.
    """
    events = fetch_historical_events(api_key_events, year, month, day)
    if not events:
        print("No historical events found.")
        return

    for event in events:
        description = event.get('event', '')
        print(f"Event: {description}")
        if description:
            image_urls = fetch_images_with_serpapi(description, api_key_images, num_images)
            for img_url in image_urls:
                print(f"Image URL: {img_url}")

# Example Usage
api_key_hist_events = 'c7iW1X/NBQzSqGPB3dtMrg==23f1sq2apRjQlupn'
api_key_serp = 'f5ac244fa02c5d4a5e353641550f68a99ec0569ae8b2440354d44e6c636b829d'
fetch_events_and_images(api_key_hist_events, api_key_serp, 1969)