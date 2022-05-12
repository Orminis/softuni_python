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



# def is_perfect(some_number):
#     sum = 0
#     list_of_sum = []
#     for divisor in range(1, some_number):
#         if some_number % divisor == 0:
#             sum += divisor
#             list_of_sum.append(sum)
#     if sum == some_number:
#         return f"We have a perfect number! \n {list_of_sum}"
#     return f"It's not so perfect. \n {list_of_sum}"
#
#
# number = int(input())
# print(is_perfect(number))
