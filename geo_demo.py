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

def get_distance(loc1, loc2):
	return geodesic((get_latitude(loc1), get_longitude(loc1)), (get_latitude(loc2), get_longitude(loc2))).miles

while True:
	loc = input("Enter a location identifier: ")

	print(get_address(loc))
	print()

	if input("Continue? ") == 'n':
		print()
		break
	else:
		print()

while True:
	lat = float(input("Enter the latitude: "))
	lon = float(input("Enter the longitude: "))

	print(get_address_by_coords(lat, lon))
	print()

	if input("Continue? ") == 'n':
		print()
		break
	else:
		print()

while True:
	loc1 = input("Enter the starting location: ")
	loc2 = input("Enter the ending location: ")

	print("%s miles" %(round(get_distance(loc1, loc2)) ))
	print()
	
	if input("Continue? ") == 'n':
		print()
		break
	else:
		print()