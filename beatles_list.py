beatles = ["John", "Paul", "George", "Ringo"]
while True:
    command = input("Please enter command (a/p/s/d): ").strip()
    match command:
        case "a":
            name = input("Please enter name of new band member: ").strip()
            beatles.append(name)
        case "p":
            print("Members of the Beatles: ")
            for member in beatles:
                print(member)
        case "s":
            name = input("Please enter name of band member to find: ").strip()
            if name in beatles:
                print(name, "is in the Beatles!")
            else:
                print(name, "is not in the Beatles")
        case "d":
            name = input("Please enter name of band member to remove: ").strip()
            if name in beatles:
                beatles.remove(name)
            else:
                print(name, "is not in the Beatles")
        case _:
            print("Unknown command")
        