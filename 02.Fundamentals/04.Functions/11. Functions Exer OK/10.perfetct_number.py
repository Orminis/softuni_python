"""
A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
"""

def is_perfect(some_number):
    sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            sum += divisor
    if sum == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))
#
#
# def is_perfect(some_number):
#     list_of_divisors = []
#     for divisor in range(1, some_number):
#         if some_number % divisor == 0:
#             list_of_divisors.append(divisor)
#
#     divisor_sum = sum(list_of_divisors)
#
#     if divisor_sum == some_number:
#         return f"We have a perfect number! \n {list_of_divisors}"
#     return f"It's not so perfect. \n {list_of_divisors}"
#
#
# number = int(input())
# print(is_perfect(number))
