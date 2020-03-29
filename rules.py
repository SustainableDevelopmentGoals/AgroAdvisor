from business_rules import export_rule_data,run_all
from WeatherVariables import WeatherVariables
from AgriActions import AgriActions

export_rule_data(WeatherVariables,AgriActions)

rules = [
{ "conditions": { "all": [
      { "name": "rainfall_total",
        "operator": "greater_than",
        "value": 30,
      }
  ]},
  "actions": [
      { "name": "high_rain" },
  ],
},
{"conditions": {"all": [
    {"name": "rainfall_total",
     "operator": "less_than",
     "value": 30,
     }
]},
    "actions": [
        {"name": "low_rain"},
    ],
}
]

def run_rules(weather):
    run_all(rule_list=rules,defined_variables=WeatherVariables(weather),defined_actions=AgriActions())