sth = input("input a word: ")
yuan = "aeiou"
fu = "bcdfghjklmnpqrstvwxyz"

for letter in yuan:
    for i in sth:
        if i == letter:
            print(sth, "yay")
            break

for charater in fu:
    for a in sth:
        if a == charater:
            print(sth, "ay")
            break



# Answer from other student

# o = input("enter a wrord: ")
# print(o)
# yuan = {"a","e","i","o","u"}
# fu = {"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"}
# word = o
# first = o[0]
# if o[0] in yuan:
#     newword = word + "ay"
# else:
#     newword = word[1:] + o[0] + "ay"

# if (o[0] and o[1]) in fu:
#     newword = word[2:] + o[0] + o[1] + "ay"

# if (o[0] and o[1] and o[2]) in fu:
#     newword = word[3:] + o[0] + o[1] + o[2] + "ay"

# print(newword)