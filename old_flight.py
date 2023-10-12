import math

excessCharge = 0

classOfTravel = input("Class of travel").upper()
if classOfTravel != "BUSINESS" and classOfTravel != "ECONOMY":
    print("ERROR: Class of travel must be \"BUSINESS\" or \"ECONOMY\"")
    exit(1)

bagWeight = math.ceil(int(input("Bag weight")))
excessCharge = 0.0

if classOfTravel == "ECONOMY":
    if bagWeight > 16:
        excessWeight = bagWeight - 16
        excessCharge += excessWeight * 5
elif classOfTravel == "BUSINESS":
    if bagWeight > 24:
        excessWeight = bagWeight - 24
        excessCharge += excessWeight * 5

print("The excess weight charge is", excessCharge)