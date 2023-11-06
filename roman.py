arabic = int(input("Arabic number: "))
letters = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
romans = []
result = ""

for roman, value in letters.items():
    fit = arabic // value
    #print(roman, "fits in", fit)
    arabic -= fit * value
    for _ in range(fit):
        result += roman

print(result)