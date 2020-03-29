from business_rules.actions import *
from business_rules.fields import *

class AgriActions(BaseActions):

    def __init__(self):
        print("t")

    #@rule_action(params={"max_advice": FIELD_NUMERIC})
    def high_rain(self):
        print("It is raining hard in the coming days")

    def low_rain(self):
        print("It is not raining hard in the coming days")
