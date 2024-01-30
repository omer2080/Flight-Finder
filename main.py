#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager


data_manager_instance = DataManager()
sheet_data = DataManager.get_sheety_data(data_manager_instance)

print("Sheet Data:")
print(sheet_data)

for row in sheet_data:
    if 'iataCode' in row and not row['iataCode']:
        from flight_search import FlightSearch as FS
        row['iataCode'] = FS.city_code_update(row['city'])

DataManager.set_sheety_data(data_manager_instance)
           
print("Sheet Data:")
print(sheet_data)
