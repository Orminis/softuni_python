import sys


def smallest_number():
    x = sys.maxsize

    for i in range(3):
        number = int(input())
        if number < x:
            x = number
    print(x)


smallest_number()


#######
def smallest_number1(some_numbers):
    return min(some_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
numbers = [first_number, second_number, third_number]
print(smallest_number1(numbers))


###############

def smallest_number2(another_numbers):
    min_num = sys.maxsize

    for number_x in another_numbers:
        if number_x < min_num:
            min_num = number_x

    return min_num


number1 = int(input())
number2 = int(input())
number3 = int(input())
list_of_numbers = [number1, number2, number3]

print(smallest_number2(list_of_numbers))

##################################################


def smallest_number3(*args):
    print(type(args))
    return min(args)


number1 = int(input())
number2 = int(input())
number3 = int(input())
list_of_numbers = [number1, number2, number3]