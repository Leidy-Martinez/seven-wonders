import requests
import time

def get_single_wonder(location):
    LOCATIONIQ_API_KEY = "Replace this with your API key"

    PATH = "https://us1.locationiq.com/v1/search.php"  

    query_params = {
      "key": LOCATIONIQ_API_KEY,
       "q": location, 
       "format": "json"
    }

    response = requests.get(PATH, params=query_params)

    body = response.json()[0]
    result = {
      "latitude": body["lat"],
      "longitude": body["lon"],
    }

    time.sleep(.5)

    return result