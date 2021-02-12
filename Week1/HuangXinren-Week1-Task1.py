number_list=[1,2,3,4,5,6.5]
print("number list:" , number_list)

def the_numbers(number_list):
    even_list=[]
    for number in number_list:
        if number % 2 == 0:
            even_list.append(number)

    return even_list
even_number = the_numbers(number_list)
print("even", even_number)


def the_numbers(number_list):
    odd_list=[]
    for number in number_list:
        if number % 2 == 1:
            odd_list.append(number)

    return odd_list
odd_number = the_numbers(number_list)
print("odd", odd_number)


