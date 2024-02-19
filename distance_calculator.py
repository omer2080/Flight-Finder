from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class DistanceCalculator:
    def get_coordinates(self, city_name):
        geolocator = Nominatim(user_agent="get_coordinates")
        location = geolocator.geocode(city_name)
        return location.latitude, location.longitude

    def calculate_distance(self, city1, city2):
        coords_city1 = self.get_coordinates(city1)
        coords_city2 = self.get_coordinates(city2)

        distance = geodesic(coords_city1, coords_city2).kilometers
        return distance

