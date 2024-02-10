#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime
from data_manager import DataManager
from flight_search import FlightSearch
flight_search = FlightSearch()


#GENERIC DATA - RELEVANT TO ALL FLIGHTS:
origin_iata_code = "TLV"
fly_date_from = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y") 
fly_date_to = (datetime.datetime.now() + datetime.timedelta(days=180)).strftime("%d/%m/%Y")
min_nights = 3
max_nights = 6
num_of_cheapests_flights_per_city = 1
stopovers = 0
currency = "USD"


# UNCOMMENT THE NEXT LINES IF NEEDED AND COMMENT THE CURRENT "sheet_data":
# (I COMMENTED IT TO PREVENT GETTING TO QUOTA LIMIT AND THEN GETTING AN ERROR)

# data_manager_instance = DataManager()
# sheet_data = DataManager.get_sheety_data(data_manager_instance)
sheet_data = [{'city': 'Amsterdam', 'iataCode': 'AMS', 'lowestPrice': 130, 'id': 2}, {'city': 'Athens', 'iataCode': 'ATH', 'lowestPrice': 100, 'id': 3}, {'city': 'Bangkok', 'iataCode': 'BKK', 'lowestPrice': 650, 'id': 4}, {'city': 'Budapest', 'iataCode': 'BUD', 'lowestPrice': 60, 'id': 5}, {'city': 'Lisbon', 'iataCode': 'LIS', 'lowestPrice': 130, 'id': 6}, {'city': 'London', 'iataCode': 'LON', 'lowestPrice': 90, 'id': 7}, {'city': 'Madrid', 'iataCode': 'MAD', 'lowestPrice': 90, 'id': 8}, {'city': 'Prague', 'iataCode': 'PRG', 'lowestPrice': 70, 'id': 9}, {'city': 'Rome', 'iataCode': 'ROM', 'lowestPrice': 70, 'id': 10}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 750, 'id': 11}]

# for row in sheet_data:
#     if 'iataCode' in row and not row['iataCode']:
#         from flight_search import FlightSearch as FS
#         row['iataCode'] = FS.city_code_update(row['city'])

# DataManager.set_sheety_data(data_manager_instance)
           
print("")
print(sheet_data)

for location in sheet_data:
    #receiving all data about the flight
    cheapest_flight_of_location = flight_search.check_flights(
        origin_iata_code,
        location['iataCode'],
        min_nights,
        max_nights,
        num_of_cheapests_flights_per_city,
        fly_date_from,
        fly_date_to,
        stopovers,
        currency,
        location['lowestPrice']
    )
    #sending a mail with details about the flight
    from notification_manager import NotificationManager
    if cheapest_flight_of_location is not None:
        my_mail_data = NotificationManager(cheapest_flight_of_location)
        my_mail_data.mail_sender()
    
    
    
    
    
