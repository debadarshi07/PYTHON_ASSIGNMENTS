room_type = input("Enter room type('Standard' or 'Deluxe' or 'Suite'): ")
duration_of_stay = int(input("Enter no. of nights: "))
season = input("Enter the season('Winter' or 'Other'): ")
is_loyalty_member = input("Are you a loyalty member('Y' or 'N'): ")

room_cost = 0
match room_type.lower():
    case 'standard':
        room_cost = 100
    case 'deluxe':
        room_cost = 150
    case 'suite':
        room_cost = 250
    case _:
        print("Invalid room type")
        exit()

duration_discount = 0
if duration_of_stay > 7:
    duration_discount = room_cost * 0.20
elif duration_of_stay > 3:
    duration_discount = room_cost * 0.10

season_discount = 0
if season.lower() == 'winter':
    season_discount = -room_cost * 0.20
else :
    season_discount = room_cost * 0.15

loyalty_member_discount = 0
if is_loyalty_member.lower() == 'y':
    loyalty_member_discount = room_cost * 0.05

final_cost = room_cost - duration_discount - season_discount - loyalty_member_discount
print(f"The final booking will cost you ${final_cost} only.")