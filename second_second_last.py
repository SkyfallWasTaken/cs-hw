word = input("Please enter your word: ")
if len(word) < 5:
    print("Word is too short")
else:
    print("Second letter:", word[1])
    print("Second last letter:", word[-2])