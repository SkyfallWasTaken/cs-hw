quantity = float(input("Quantity of drug (in mg)"))
hours = 0

while quantity > 0.1:
    quantity *= 0.95
    hours += 1

print("Next dose required after", hours, "hours")