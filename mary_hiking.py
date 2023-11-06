daily_hiking_miles = []
for day in range(1, 6):
    daily_hiking_miles.append(
        float(
            input(
                "Day "
                + str(day)
                + " of hiking: please enter hiking distance in miles: "
            )
        )
    )

print("Hiking distance in kilometres =", sum(daily_hiking_miles) * 1.61)
