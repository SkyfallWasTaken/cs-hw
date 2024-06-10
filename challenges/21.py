number = float(number)
user_input = int(input("1) centimetres to inches\n2) inches to centimetres\nChoose your mode: ").strip())

if user_input == 1:
    print(user_input, "cm =", number * 0.3937007787, "in")
else:
    print(user_input, "in =", number * 2.54, "cm")