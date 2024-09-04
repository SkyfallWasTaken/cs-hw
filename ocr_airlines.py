import math

tracking_code = input("Enter a tracking code: ").upper()
if len(tracking_code) == 8 and (tracking_code[0] == "P" or tracking_code[0] == "Q"):
    print("VALID")
else:
    print("INVALID")

luggage_weight = float(input("Enter luggage weight (in kg): "))
if luggage_weight > 50:
    print("Error: luggage weight is over 50kg.")
else:
    print(f"Price: £{math.ceil(luggage_weight) * 3}")
