x = int(input("x"))
y = int(input("y"))
z = int(input("z"))

if (x > y) or y < z:
    print("1")
elif x < y and y > z:
    print("2")
else:
    print("3")
