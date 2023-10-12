import math

excessCharge = 0
classOfTravel = input("Class of travel").upper()
if classOfTravel != "BUSINESS" and classOfTravel != "ECONOMY":
    print("ERROR: Class of travel must be \"BUSINESS\" or \"ECONOMY\"")
    exit(1)

baggageWeight = math.ceil(float(input("Baggage weight")))
if baggageWeight > 40:
    print("ERROR: Baggage weight must be under 40kg")
    exit()

if classOfTravel == "ECONOMY" and baggageWeight > 12:
    print("Excess baggage charge is", (baggageWeight - 12) * 6)
elif classOfTravel == "ECONOMY" and baggageWeight > 28:
    print("Excess baggage charge is", (baggageWeight - 28) * 3.50)
else:
    print("No excess baggage")