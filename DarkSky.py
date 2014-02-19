import forecastio
import datetime as dt
import pytz


api_key = '65923ecf51cb60d1e9094af9d356287e'

lat= 40.7833
lon= -73.9667

class DarkSky(api_key, lat, lon, loc_tz=tz.timezone('America/New_York')):
    self.api_key = api_key
    self.lat = lat
    self.lon = lon
    self.loc_tz = loc_tz


    def get_data(api_key, lat, lon, time=None):

    forecast = forecastio.load_forecast(api_key, lat, lon)

    past_date = dt.datetime(2000, 7, 4, 0, 1, 1, tzinfo=loc_tz)
    hist_forecast = forecastio.load_forecast(api_key, lat, lon, past_date)
    dir(forecast)
    utc_dt = pytz.utc.localize(dt.datetime.utcfromtimestamp(utc_time))
    loc_dt = loc_tz.normalize(utc_dt.astimezone(loc_tz))
    
    



