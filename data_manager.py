import requests

sheety_url = "https://api.sheety.co/e76501e944cf045c8721dd7fcbb75a9f/myFlightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.    
    
    def __init__(self) -> None:
        self.sheety_data = {}

    def get_sheety_data(self):
        response = requests.get(sheety_url)
        data = response.json()
        self.sheety_data = data['prices']
        return self.sheety_data
    
    def set_sheety_data(self):
        for city in self.sheety_data:
            body = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                f"{sheety_url}/{city['id']}",
                json=body,  
                headers={
                    "Content-Type": "application/json"  # Set the Content-Type header explicitly
                }
            )
            print(response.text)
