import requests
import os
from dotenv import load_dotenv

load_dotenv()

tequila_url = "https://tequila-api.kiwi.com"
my_api = os.getenv("my_api_key")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    #The function returns the IATA code of the city 
    def city_code_update(city_name):
        data_url = f"{tequila_url}/locations/query"
        headers = {"apikey": my_api}
        params = {"term": city_name, "location_types": "city"}
        response = requests.get(url=data_url, headers=headers, params=params)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
            
        