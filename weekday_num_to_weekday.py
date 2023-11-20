weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
number = int(input("Please enter weekday number: "))
if number > 7 or number < 0:
    print("Invalid weekday number")
else:
    print(weekdays[number])
