from business_rules.variables import *

class WeatherVariables(BaseVariables):

    def __init__(self,weather_info):
        self.weather = weather_info

    @numeric_rule_variable
    def rainfall_total(self):
        return self.weather.total_rainfall()

    @numeric_rule_variable
    def avg_temperature(self):
        return self.weather.avg_temperature_day()

    @numeric_rule_variable
    def max_wind_speed(self):
        return self.weather.max_wind_speed()