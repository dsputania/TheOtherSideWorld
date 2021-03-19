from folium import Map,Popup
from main import Geopoint

#Get latitude and longitude values
latitude = 24.882618
longitude = 72.858894

#Folium Map instance
mymap = Map(location= [latitude,longitude])

#Create a Geopoint instance
geopoint = Geopoint(latitude= latitude, longitude= longitude)
forecast = geopoint.get_weather()
popup_content = f"""
{forecast[0][0][11:13]}h: {forecast(round([0][1]))}° <img src = "http://openweathermap.org/img/wn/{forecast[0][3]}@2x.png" width=35>
<hr style= "margin:1px">
{forecast[1][0][11:13]}h: {forecast(round([1][1]))}° <img src = "http://openweathermap.org/img/wn/{forecast[1][3]}@2x.png" width=35>
<hr style= "margin:1px">
{forecast[2][0][11:13]}h: {forecast(round([2][1]))}° <img src = "http://openweathermap.org/img/wn/{forecast[2][3]}@2x.png" width=35>
<hr style= "margin:1px">
{forecast[3][0][11:13]}h: {forecast(round([3][1]))}° <img src = "http://openweathermap.org/img/wn/{forecast[3][3]}@2x.png" width=35>
"""


print(forecast[0][0][11:13])
popup = Popup(popup_content, max_width= 400)
popup.add_to(geopoint)
geopoint.add_to(mymap)


#Save the Map instance in a HTML file
mymap.save("dd.html")


print(mymap)













