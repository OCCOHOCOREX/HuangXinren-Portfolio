# Task 2


letters = ["a","b","c","d","e"]
# for i in range(0,5):
#     print(letter[i])

text = "Given a string of text, print the number of times each letterin the alphabets a-z appear."

alph = "abcdefghijklmnopqrstuvwxyz"

for letter in alph:
    count = 0

    for i in text.lower():
        if i == letter:
            count += 1

    print(letter + "=" + str(count))

