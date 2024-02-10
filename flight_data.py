class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, destination_city, destination_airport, depart_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.depart_date = depart_date
        self.return_date = return_date
        