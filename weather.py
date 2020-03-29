import requests
import json
import rules
from WeatherObject import WeatherForecast

def get_field(data,field):
    if field in data.keys():
        return data[field]

api_key = "2ed2550d1c52b0f18c42da83167f970b"
api_base = "http://api.openweathermap.org/data/2.5/"

forecast_string = "forecast?"
metric_string = "&units=metric"
apikey_string = "&appid="

city = "q=Addis Abeba"
lat = "lat=-3.4653&lon=-62.2159"

request_string = api_base+forecast_string+lat+metric_string+apikey_string+api_key
print(request_string)
forecast = json.loads(requests.get(request_string).content)
weather = WeatherForecast(forecast)
rules.run_rules(weather)

