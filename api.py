import googlemaps
from geocoding import geoloc_list_lat
from geocoding import geoloc_list_lng
API_KEY = 'ENTER API KEY'
google_maps = googlemaps.Client(key=API_KEY)

result = []

def placeapi():
    for i in range(len(geoloc_list_lng)):
        places= []
        combined = ''
        cordnate = str(geoloc_list_lat[i]) + ',' + str(geoloc_list_lng[i])
        try:
            places= gmaps.places_nearby(location=cordnate, radius=300, open_now=False, type='restaurant')
        except KeyError:
            pass
        for i in places['results']:
            id = i['place_id']
            parameters = ['name', 'formatted_address']
            places_details = gmaps.place(place_id=id, fields=parameters)
            result = places_details['result']
            address = result['formatted_address']
            names = result['name']
            combined += ' ' + names + ' @ ' + address + ' --- '
        results.append(combined)
