gas_bill = float(input("Gas bill: "))
electric_bill = float(input("Electric bill: "))

if (gas_bill + electric_bill) > 10:
    global total_bill
    total_bill = (gas_bill + electric_bill) * 0.95
else:
    total_bill = gas_bill + electric_bill
print(total_bill)