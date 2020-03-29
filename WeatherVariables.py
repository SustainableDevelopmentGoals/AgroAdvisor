from business_rules.variables import *

class WeatherVariables(BaseVariables):

    def __init__(self,weather_info):
        self.weather = weather_info

    @numeric_rule_variable
    def rainfall_total(self):
        return self.weather.total_rainfall()