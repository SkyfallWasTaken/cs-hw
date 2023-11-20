orig_secs = int(input("Please enter a number of seconds: "))

hours = orig_secs // (60 * 60)
orig_secs -= hours * (60 * 60)

minutes = orig_secs // 60
orig_secs -= minutes * 60

seconds = orig_secs

print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
