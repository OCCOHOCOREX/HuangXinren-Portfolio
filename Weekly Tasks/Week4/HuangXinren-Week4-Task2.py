list = ["comfortable", "round", "support", "machinery"]
p1 = list[0::2]
s1 = " ".join(p1)
print(s1)

p2 = list[0::3]
s2 = " ".join(p2)
print(s2)

p3 = list[1:3]
s3 = " ".join(p3)
print(s3)

p4 = list[1::2]
s4 = " ".join(p4)
print(s4)


# Key answer from students

# words = ["comfortable", "round", "support", "machinery"]
# i = 0
# l = 0
# for word1 in words:
#     for word2 in words:
#         if word1 != word2:
#             print(str(word1) + " " + str(word2))

# The operator '!=' in python takes the thing on the 
# left hand side of itself and the thing on the right 
# hand side of itself, and returns True if they are not equal, 
# and false if they are equal.