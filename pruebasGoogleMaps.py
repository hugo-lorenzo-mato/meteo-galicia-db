# "API_KEY: AIzaSyCY23bGoC9rUgPYuwAu6JqseIKn2Jq9hRE"
'''
from googlemaps import GoogleMaps

gmaps = GoogleMaps("AIzaSyCY23bGoC9rUgPYuwAu6JqseIKn2Jq9hRE")
reverse = gmaps.reverse_geocode(38.887563, -77.019929)
address = reverse['Placemark'][0]['address']
print(address)
accuracy = reverse['Placemark'][0]['AddressDetails']['Accuracy']
print(accuracy)
'''