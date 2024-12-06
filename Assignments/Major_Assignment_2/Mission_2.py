# Mission - 2 (High Alert Identification)

from Mission_1 import cleaned_list

previous_intel = {"Kyiv", "Mariupol", "Crimea", "Odessa", "Donetsk", "Luhansk", "Bakhmut"}

aid_requiring_cities = previous_intel.union(cleaned_list)
# print(f"\nAid requiring cities: {aid_requiring_cities}")

low_alert_cities = previous_intel ^ set(cleaned_list)
# print(f"\nLow alert cities: {low_alert_cities}")

high_alert_cities = previous_intel.intersection(cleaned_list)
# print(f"\nHigh alert cities: {high_alert_cities}\n")