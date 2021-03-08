from folium import Map

latitude = 40.09
longitude = -3.47

antipode_latitude = latitude * -1

if longitude < 0:
    antipode_longitude = longitude + 180
elif longitude == 0:
    antipode_longitude = 180
elif longitude > 180:
    antipode_longitude = "Invalid value"
else:
    antipode_longitude = longitude - 180

location = [antipode_latitude,antipode_longitude]
mymap = Map(location)
mymap.save("antipode.html")

print(antipode_latitude)
print(antipode_longitude)
print(mymap)
