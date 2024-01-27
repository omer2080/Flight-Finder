import requests
from pprint import pprint
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    sheety_url = "https://api.sheety.co/e76501e944cf045c8721dd7fcbb75a9f/myFlightDeals/prices"

    def get_sheety_data(api_url):
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            # Assuming Sheety returns JSON data
            data = response.json()

            return data, api_url

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None, api_url

    # Example usage
    sheety_data, sheety_url = get_sheety_data(sheety_url)

    if sheety_data:
        print("Sheety Data:")
        pprint(sheety_data)
