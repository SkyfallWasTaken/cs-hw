salary = int(input("Salary"))
if salary <= 10_000:
    print("No tax required!")
    exit()

tax = (salary - 10_000) * 0.20
print("Final salary is", salary - tax)