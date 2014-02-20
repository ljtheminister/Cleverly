#import forecastio
import datetime as dt
import pytz
import urllib2
import json

import pyodbc
cnxn = pyodbc.connect("DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'")


api_key = '65923ecf51cb60d1e9094af9d356287e'

lat= 40.7833
lon= -73.9667

base_url = 'https://api.forecast.io/forecast/'
url = '%s%s/%s,%s'%(base_url, api_key, lat, lon)

response = urllib2.urlopen(url)
data = json.load(response)

https://api.forecast.io/forecast/65923ecf51cb60d1e9094af9d356287e/42,-74,2013-05-06T12:00:00-0400


hourly_list = []
for hourly_data in data['hourly']['data']:
    hourly_list.append(tuple(hourly_data.values()))




#CURRENTLY
'ozone'
'temperature'
'dewPoint'
'nearestStormDistance'
'cloudCover'
'humidity'
'nearestStormBearing'
'summary'
'apparentTemperature'
'pressure'
'windSpeed'
'precipProbability'
'visibility'
'time'
'windBearing'
'precipIntensity'
'icon'

#HOURLY
'ozone'
'temperature'
'icon'
'dewPoint'
'humidity'
'visibility'
'summary'
'apparentTemperature'
'pressure'
'windSpeed'
'cloudCover'
'time'
'windBearing'
'precipIntensity'
'precipProbability'



class DarkSky(api_key, lat, lon, loc_tz=pytz.timezone('America/New_York'), spec_date=None):
    self.api_key = api_key
    self.lat = lat
    self.lon = lon
    self.loc_tz = loc_tz
    self.base_url = 'https://api.forecast.io/forecast/'
    self.spec_date = spec_date
    if self.spec_date == None:
	self.url = '%s%s/%s,%s'%(base_url, api_key, lat, lon)
    else:
	self.url = '%s%s/%s,%s'%(base_url, api_key, lat, lon, self.spec_date)




    def get_data(api_key, lat, lon, time=None):

    forecast = forecastio.load_forecast(api_key, lat, lon)

    past_date = dt.datetime(2000, 7, 4, 0, 1, 1, tzinfo=loc_tz)
    hist_forecast = forecastio.load_forecast(api_key, lat, lon, past_date)
    dir(forecast)
utc_dt = pytz.utc.localize(dt.datetime.utcfromtimestamp(utc_time))
loc_dt = loc_tz.normalize(utc_dt.astimezone(loc_tz))
    
    



