# Mission - 1 (Clearing the Field)

def remove_duplicates_and_sort(city_list):
    set_of_cities = set(city for city in city_list)
    cleaned_list = sorted(list(set_of_cities))
    return cleaned_list

cities = ["Kyiv", "Kherson", "Kharkiv", "Odessa", "Poltava", "Kherson", "Lviv", "Kharkiv", "Crimea", "Odessa"]
cleaned_list = remove_duplicates_and_sort(cities)
# print(f"\nCleaned list: {cleaned_list}\n\n")