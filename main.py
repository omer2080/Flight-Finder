#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime
import getpass
from data_manager import DataManager
from flight_search import FlightSearch
flight_search = FlightSearch()

#password for connecting the mail and sending a message of the deals:
PASSWORD = getpass.getpass("Enter The Mail Password: ")


#GENERIC DATA - RELEVANT TO ALL FLIGHTS:
origin_iata_code = "TLV"
fly_date_from = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y") 
fly_date_to = (datetime.datetime.now() + datetime.timedelta(days=180)).strftime("%d/%m/%Y")
min_nights = 3
max_nights = 6
num_of_cheapests_flights_per_city = 1 # how many offers the programs returns (for each city)
stopovers = 0
currency = "USD"


# UNCOMMENT THE NEXT LINE IF YOU HAVE A QUOTA LIMIT ERROR (it might happen if we send too many API requests):
# sheet_data = [{'city': 'Amsterdam', 'iataCode': 'AMS', 'lowestPrice': 130, 'id': 2}, {'city': 'Athens', 'iataCode': 'ATH', 'lowestPrice': 200, 'id': 3}, {'city': 'Bangkok', 'iataCode': 'BKK', 'lowestPrice': 650, 'id': 4}, {'city': 'Budapest', 'iataCode': 'BUD', 'lowestPrice': 60, 'id': 5}, {'city': 'Lisbon', 'iataCode': 'LIS', 'lowestPrice': 130, 'id': 6}, {'city': 'London', 'iataCode': 'LON', 'lowestPrice': 90, 'id': 7}, {'city': 'Madrid', 'iataCode': 'MAD', 'lowestPrice': 90, 'id': 8}, {'city': 'Prague', 'iataCode': 'PRG', 'lowestPrice': 70, 'id': 9}, {'city': 'Rome', 'iataCode': 'ROM', 'lowestPrice': 70, 'id': 10}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 750, 'id': 11}]

    # if you uncommented the previous line - put in comment the whole next part (all until next printing)

data_manager_instance = DataManager()
sheet_data = DataManager.get_sheety_data(data_manager_instance)
print(f'\nMy Flight Deals Without IataCode:\n{sheet_data}')

for row in sheet_data:
    if 'iataCode' in row and not row['iataCode']:
        from flight_search import FlightSearch as FS
        row['iataCode'] = FS.city_code_provider(row['city'])

DataManager.set_sheety_data(data_manager_instance)
           
print(f'\nMy Flight Deals After Filling IataCode:\n{sheet_data}')

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
        location['lowestPrice'],
    )
    #sending a mail with details about the flight
    from notification_manager import NotificationManager
    if cheapest_flight_of_location is not None:
        my_mail_data = NotificationManager(cheapest_flight_of_location)
        my_mail_data.mail_sender(PASSWORD)
    
    
    
    
    
