from business_rules import export_rule_data,run_all
from WeatherVariables import WeatherVariables
from AgriActions import AgriActions

export_rule_data(WeatherVariables,AgriActions)

rules = [
{ "conditions": { "all": [
      { "name": "rainfall_total",
        "operator": "greater_than_or_equal_to",
        "value": 30,
      }
  ]},
  "actions": [
      { "name": "high_rain" },
  ],
},
{"conditions": {"all": [
    {
        "name": "rainfall_total",
         "operator": "less_than",
         "value": 30,
    },
    {
        "name": "rainfall_total",
        "operator": "greater_than",
        "value": 0,
    }
]},
    "actions": [
        {"name": "low_rain"},
    ],
},
{"conditions": {"all": [
    {
        "name": "rainfall_total",
         "operator": "equal_to",
         "value": 0,
    },
    {
        "name": "max_wind_speed",
         "operator": "less_than",
         "value": 29,
    }

]
},
    "actions": [
        {"name": "no_rain_wind"},
    ],
},
{"conditions": {"all": [
    {
         "name": "avg_temperature",
         "operator": "greater_than",
         "value": 30,
    }

]
},
    "actions": [
        {"name": "high_temp_no_rain"},
    ],
}
]

def run_rules(weather):
    actions = AgriActions()
    run_all(rule_list=rules,defined_variables=WeatherVariables(weather),defined_actions=actions)
    return actions.advice