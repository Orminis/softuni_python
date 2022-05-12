def rounding():
    numbers = input().split()
    new_list = []

    for i in range(len(numbers)):
        x = round(float(numbers[i]))
        new_list.append(x)

    print(new_list)


rounding()


