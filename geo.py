from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder

class Geopoint:
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

    def closest_parallel(self):
        return round(self.latitude)

    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat=self.latitude,lng=self.longitude)
        myname = 






