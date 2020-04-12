class WeatherObject:

    def __init__(self,date,time,temp,pressure,humidity,rain,wind):
        self.date = date
        self.time = time
        self.temp = temp
        self.pressure = pressure
        self.humidity = humidity
        self.rain = rain
        self.wind = wind

class WeatherForecast:

    def __init__(self,forecast):
        objects = []
        for date in forecast["list"]:
            date_time = date["dt_txt"].split(" ")
            date_txt, time_txt = date_time
            temp = date["main"]["temp"]
            pressure = date["main"]["pressure"]
            humidity = date["main"]["humidity"]
            rain = date["rain"]["3h"] if "rain" in date.keys() else 0
            wind = date["wind"]
            weather_object = WeatherObject(date_txt,time_txt,temp,pressure,humidity,rain,wind)
            objects.append(weather_object)
        self.objects = objects

    def total_rainfall(self):
        total_rainfall = 0
        for object in self.objects:
            total_rainfall += object.rain
        return round(total_rainfall,2)

    def max_wind_speed(self):
        return round(max([obj.wind["speed"] for obj in self.objects]),2)

    def avg_temperature_day(self):
        temps = [obj.temp for obj in self.objects if 10 < int(obj.time.split(":")[0]) < 20]
        avg_temp = sum(temps)/len(temps)
        return round(avg_temp,2)

    def to_json(self):
        json = {'total_rainfall':self.total_rainfall(), 'max_wind_speed':self.max_wind_speed(), 'avg_temperature_day':self.avg_temperature_day() }
        return json