import requests
import os
from dotenv import load_dotenv

from flight_data import FlightData

load_dotenv()

tequila_url = "https://tequila-api.kiwi.com"
my_api = os.getenv("my_api_key")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    #The function returns the IATA code of the city 
    def city_code_provider(city_name):
        data_url = f"{tequila_url}/locations/query"
        headers = {"apikey": my_api}
        params = {"term": city_name, "location_types": "city"}
        response = requests.get(url=data_url, headers=headers, params=params)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_iata_code, destination_iata_code, min_nights, max_nights, num_of_cheapests_flights_per_city, fly_date_from, fly_date_to, stopovers, currency, max_price_to_pay):
        if destination_iata_code == 'BKK' or destination_iata_code == 'SYD':
            min_nights = 10
            max_nights = 20
        headers = {"apikey": my_api}
        query = {
            "fly_from": origin_iata_code,
            "fly_to": destination_iata_code,
            "date_from": fly_date_from,
            "date_to": fly_date_to,
            "nights_in_dst_from": min_nights,
            "nights_in_dst_to": max_nights,
            "one_for_city": num_of_cheapests_flights_per_city,
            "max_stopovers": stopovers,
            "curr": currency,
            "price_to": max_price_to_pay 
        }
        return self.check_flights_get_request(headers, query, destination_iata_code)
    
    def check_flights_get_request(self, headers, query, destination_iata_code):        
        response = requests.get(
            url=f"{tequila_url}/v2/search",
            headers=headers,
            params=query,
        )
        try:
            flight_data_list = response.json()["data"][0]
        except IndexError:
            print(f"No flights for {destination_iata_code}.")
            return None
        
        flight_data = FlightData(
            price = flight_data_list["price"],
            origin_city = "Tel Aviv",
            destination_city = flight_data_list["route"][0]["cityTo"],
            destination_airport = flight_data_list["route"][0]["flyTo"],
            depart_date = flight_data_list["route"][0]["local_departure"].split("T")[0],
            return_date = flight_data_list["route"][1]["local_departure"].split("T")[0],
            flight_link = flight_data_list["booking_token"]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
    
    
    
        
        
        
            
    