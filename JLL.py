import folium
from geocoding import name_lst
from geocoding import loopThruCSV
from geocoding import geoloc_list_lng
from geocoding import geoloc_list_lat
from geocoding import avgP
from geocoding import submarket
from api import stored_results
from api import placeapi
m = folium.Map(location =[41.8781, -87.6298], zoom_start = 9)

loopThruCSV("DataSample.csv")
placeapi()

#print(len(name_lst))
for name in range(len(name_lst)):
        myString = 'Building Name/Address: {} <br/> Average Rent: {} <br/> <br/> <br/> Restaurants Nearby: <br/> {}'.format(name_lst[name], avgP[name], stored_results[name])
        submarketString = 'Submarket: {}'.format(submarket[name])
        folium.Marker([geoloc_list_lat[name], geoloc_list_lng[name]],
                popup = folium.Popup(html= myString, max_width=800),
                tooltip=submarketString, icon = folium.Icon(color='darkred', icon='info-sign')).add_to(m)

m.save('map.html')