import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(timeout=9, user_agent="jllhacksiii")

location = geolocator.geocode("1 Mid America Plaza, illinois")
#print(location.latitude)

geoloc_list_lat = []
geoloc_list_lng = []
name_lst = []
avgP = []
submarket = []

file_name = "AvailabilityDataSamples.csv"
file_name_output = "DataSample2.csv"
df = pd.read_csv(file_name, sep=",")
df.drop_duplicates(subset="PropertyID", inplace=True)
df.to_csv(file_name_output)

def loopThruCSV(filename):
    count = 0
    infile = open(filename, encoding='utf-8').readlines()
    for i in range(0,len(infile)):
        col = infile[i].split(',')
        if "Address" in col[2]:
            continue
        if "940" in col[6]:
            continue
        if "1 Overlook" in col[2]:
            continue
        if "1000 E Warrenville Rd" in col[2]:
            continue
        if "1 Pierce Pl" in col[2]:
            continue
        if "1000 Milwaukee Ave" in col[2]:
            continue
        if "1000 Remington Blvd" in col[2]:
            continue
        if "1155 W Fulton St" in col[2]:
            continue
        if "1440-1472 Market St" in col[2]:
            continue
        if "2 Mid America" in col[2]:
            continue
        if "2 Overlook Pt" in col[2]:
            continue
        if "2000 W AT&T Dr" in col[2]:
            continue
        if "2135 CityGate Ln" in col[2]:
            continue
        if "225 W Wacker Dr" in col[2]:
            continue
        if "26525 N Riverwoods Blvd" in col[2]:
            continue
        if "333 W Wacker Dr" in col[2]:
            continue
        if "485 E Half Day Rd" in col[2]:
            continue
        if "600 N US Hwy 45" in col[2]:
            continue
        if "8 N Pkwy Blvd" in col[2]:
            continue
        if "915-939 W North Ave" in col[2]:
            continue
        else:
            geoInput = (col[2] + ", " + col[6])
            #print(geoInput)
            location = geolocator.geocode(geoInput)
            latVal = location.latitude
            geoloc_list_lat.append(latVal)
            lngVal = location.longitude
            geoloc_list_lng.append(lngVal)
            name_lst.append(col[3])
            lowPriceTmp = col[35]
            highPriceTmp = col[36]
            if ("$" in lowPriceTmp) and ("$" in highPriceTmp) and ("-" not in lowPriceTmp):
                lowPriceTmp = float(lowPriceTmp[1:])
                highPriceTmp = float(highPriceTmp[1:])
                avgPrice = float((highPriceTmp + lowPriceTmp) / 2)
                avgPrice = ('$' + str(avgPrice)) + ' ' + 'Per Sq/Foot'
                avgP.append(avgPrice)
            else:
                avgP.append("Not Available")
            submarket.append(col[10])

            #print(avgPrice)
            #print(location.latitude, location.longitude, col[2])
            count = count + 1
            #print(count)


loopThruCSV("DataSample.csv")

#print(len(name_lst))