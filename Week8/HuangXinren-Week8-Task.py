import sys

#print(sys.argv[1:])
operation = sys.argv[1]

def sum_numbers(nums):
    nums = [2, 10 ,11 ,1]
    return sum(nums)

numbers_to_sum = [int(i) for i in sys.argv[2:]]

if operation == "add":
    print(sum_numbers(numbers_to_sum))
elif operation == "multiply":
    def multiplylist(inputlist):
        output = 1
        correctoutput = Flase
        for element in inputlist:
            if type(element) ==int:
                correctoutput = True
                output = output * element
        return output if correctoutput else None
    print(multiplylist(numbers_to_sum))


#

import sys

arguments = sys.argv[1:]
input_file = ""
output_file = ""

for i, arg in enumerate(arguments):
    if arg == "-i":
        input_file = arguments[i+1]
    elif arg == "-o":
        output_file = arguments[i+1]

with open(input_file, mode="r") as file:
    lines = file.readlines()
    lines = [int(line.strip()) for line in lines]

with open(output_file, mode="w") as output:
    output.write(str(sum(lines)))