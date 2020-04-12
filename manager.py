import os
import weather
import json
import rules

DEFAULT_FILE = "registrations.csv"
DEFAULT_WEATHER = "weather_advice.csv"
def append_registration(registration):
    advice = get_advice_registration(registration)
    with open(DEFAULT_FILE,"a") as file:
        registration["weather_advice"] = advice
        file.write(json.dumps(registration)+"\n")
        file.close()

def get_registrations():
    with open(DEFAULT_FILE,"r") as reader:
        lines = reader.readlines()
        return [json.loads(l) for l in lines]

def get_advice_registration(registration):
    weather_info = weather.get_by_latlon(registration)
    advice_string = rules.run_rules(weather_info)
    json_string = {'weather_info':weather_info.to_json(),'advice':advice_string}
    return json_string
# def send_advice_all():
#     registrations = get_registrations()
#     for registration in registrations:


