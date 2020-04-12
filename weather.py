import requests
import json
from WeatherObject import WeatherForecast
import rules

API_KEY = "2ed2550d1c52b0f18c42da83167f970b"
API_BASE = "http://api.openweathermap.org/data/2.5/forecast?units=metric&appid="+API_KEY+"&"

# forecast_string = "forecast?"
# metric_string = "&"
# apikey_string = "&appid="

# city = "q=Addis Abeba"
# lat = "lat=-3.4653&lon=-62.2159"

def get_by_latlon(registration):
    lat = registration["lat"]
    lon = registration["lon"]
    latlong = "lat=%f&lon=%f" % (lat,lon)
    request_string = API_BASE+latlong
    #print(request_string)
    forecast = json.loads(requests.get(request_string).content)
    print(forecast)
    weather_info = WeatherForecast(forecast)
    return weather_info
    # rules.run_rules(weather)

# def get_by_city(city):
#     city = "q=%s" % (city)
#     request_string = API_BASE+city
#     forecast = json.loads(requests.get(request_string).content)
#     weather = WeatherForecast(forecast)
#     print(rules.run_rules(weather))
#
# get_by_city("Kinshasa")

# request_string = api_base+forecast_string+lat+metric_string+apikey_string+api_key
# print(request_string)
