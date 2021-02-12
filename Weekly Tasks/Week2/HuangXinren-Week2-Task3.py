number = input("Please give a number: ")
b = int(number)
a = 2
while True:
    b = b - a
    if b < 0:
        print("it is not a multiple of 2")
        break
    if b == 0:
        print("it is a multiple of 2")
        break
