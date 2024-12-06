# Mission - 4 (Tracking Supply Distribution)

supplies = [("Kyiv", "Food", 500), ("Kursk", "Medicines", 200), ("Lviv", "Water", 300), ("Chelyabinsk", "Blankets", 100), ("Kharkiv", "Food", 150), ("Luhansk", "Tents", 600), ("Vladivostok", "Water", 400)]

supply_details = {details[0]: {details[1]: details[2]} for details in supplies}
print(f"Supply details: \n{supply_details}")