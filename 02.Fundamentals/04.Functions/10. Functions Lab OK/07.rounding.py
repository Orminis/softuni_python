def rounding(nums):
    new_list = []

    for i in range(len(nums)):
        x = round(float(nums[i]))
        new_list.append(x)

    return new_list


numbers = input().split()
rounded_numbers = rounding(numbers)

print(rounded_numbers)


