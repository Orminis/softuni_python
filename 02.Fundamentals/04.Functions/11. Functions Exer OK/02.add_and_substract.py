def sum_numbers(a, b):
    return a + b


def subtract(sum, num):
    return sum - num


def add_and_subtract(first_number, second_number, third_number):
    sum_of_first_two_digits = sum_numbers(first_number, second_number)
    result = subtract(sum_of_first_two_digits, third_number)
    return result


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(add_and_subtract(number1, number2, number3))
