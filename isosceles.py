Length1 = float(input("Enter the length of side 1: "))
Length2 = float(input("Enter the length of side 2: "))
Length3 = float(input("Enter the length of side 3: "))

if Length1 == Length2 or Length1 == Length3 or Length2 == Length3:
    print("Isosceles")
else:
    print("Not Isosceles")
