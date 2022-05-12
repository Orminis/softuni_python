def print_absolute_value_of_numbers():
    args = input().split(" ")
    numbers = []

    for arg in args:
        num = float(arg)
        abs_num = abs(num)
        numbers.append(abs_num)

    print(numbers)


print_absolute_value_of_numbers()
