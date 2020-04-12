from business_rules.actions import *
from business_rules.fields import *
import random

class AgriActions(BaseActions):

    def __init__(self):
        self.advice = ""

    def compile_advice(self,advice_list,k):
        advices = random.sample(advice_list,k=k)
        for advice in advices:
            self.advice += advice + "\n"

    #@rule_action(params={"max_advice": FIELD_NUMERIC})
    def high_rain(self):
        advice_list = ["Implement measures to drain excess rainfall",
                       "Plant crops with high water requirements in this period",
                       "Planting in narrow rows, with high seed densities and initial fertiliser rates",
                       "Irrigation measures can be minimized, make preparations to harvest rainwater"]
        self.compile_advice(advice_list,2)

    def low_rain(self):
        advice_list = ["Orient land preparation and pre-plant tillage towards water retention of all rainfall",
                       "Recommended to plant crops with lower water requirement",
                       "Delay planting of crops with high water requirements until the soil contains sufficient water to germinate",
                       "Wide rows (lower densities), reduced seed and fertiliser rates for more assured and costeffective food production"]
        self.compile_advice(advice_list,2)

    def no_rain_wind(self):
        advice_list = ["No rain and high wind speeds expected in the coming 5 days, applying top-dressings,fertilizers and pesticides is recommended"]
        self.compile_advice(advice_list,1)

    def high_temp_no_rain(self):
        advice_list = ["High temperatures expected with minimal rain, make preparations for irrigation"]
        self.compile_advice(advice_list,1)