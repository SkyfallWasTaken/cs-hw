# I know this is inefficient, I'm a noob at Python and made this in 5 minutes to get the job done
quote = input("Your quote: ")
words = quote.split(" ")

for (index, word) in enumerate(words):
    blank = ""
    wrote_first_letter = False
    for letter in word:
        if letter.isalpha():
            if not wrote_first_letter:
                blank += letter
                wrote_first_letter = True
            else:
                blank += "_"
        else:
            blank += letter

    words[index] = blank

print(" ".join(words))