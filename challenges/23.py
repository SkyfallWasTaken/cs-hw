import math
x = float(input("x dimension: "))
y = float(input("y dimension: "))

radius = float(input("Radius of the circle: "))
print("Area of turf needed is", (x * y) - (math.pi * radius ** 2))