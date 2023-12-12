word = input("Word to put into alternating case: ")
word_arr = list(word.lower().replace(" ", ""))

alternate = True

for (index, letter) in enumerate(word_arr):
    if alternate:
        print(alternate, letter)
        word_arr[index] = letter.upper()
        alternate = False
    else:
        alternate = True

print("".join(word_arr))