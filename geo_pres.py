from geopy.geocoders import Nominatim
from geopy.distance import geodesic

locator = Nominatim(user_agent = "GPSApp")

def get_address(identifier):   
    location = locator.geocode(identifier)
    return (location.address, location.latitude, location.longitude)

def get_address_by_coords(latitude, longitude):
    location = locator.reverse("%s,%s" % (latitude, longitude))
    return location.address

def get_latitude(identifier):
	location = locator.geocode(identifier)
	return location.latitude

def get_longitude(identifier):
	location = locator.geocode(identifier)
	return location.longitude

loc = input("Enter a location identifier: ")
print(get_address(loc))
print()

lat = float(input("Enter the latitude: "))
lon = float(input("Enter the longitude: "))
print(get_address_by_coords(lat, lon))
print()