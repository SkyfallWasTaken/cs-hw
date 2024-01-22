denary = int(input("Number in denary: "))
quotient = denary
remainders = []

while quotient != 0:
    remainders.append(str(quotient % 2))
    quotient = quotient // 2

remainders.reverse()
print(''.join(remainders))