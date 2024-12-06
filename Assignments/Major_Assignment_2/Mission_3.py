# Mission - 3 (Detailed City Intel)

from Mission_2 import high_alert_cities

city_data = [("Kyiv", 3850000, 270), ("Kharkiv", 1551000, 130), ("Lviv",524401, 190), ("Odessa", 1667050, 160), ("Bakhmut", 2335000, 60), ("Crimea", 8000000, 250), ("Luhansk", 4005000, 200)]

high_alert_cities_info = {city: details for city in high_alert_cities for details in city_data if details[0] == city}
print(f"\nInformation about the cities with high alert: {high_alert_cities_info}")

total_population = sum([details[1] for details in high_alert_cities_info.values()])
print(f"\nTotal population: {total_population}")

total_aid_requests = sum([details[2] for details in high_alert_cities_info.values()])
print(f"\nTotal aid requests: {total_aid_requests}\n")