import math

word = input("Please enter your word: ")
chars = list(word)
index = (len(word) - 1) / 2

if len(word) % 2 == 0:
    print(chars[math.floor(index)])
else:
    print(chars[int(index)])