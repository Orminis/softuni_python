def sorting_numbers(list_of_numbers):
    return sorted(list_of_numbers)     # for asc order function is sorted
                                       # for desc order sorted(list_of_numbers, reverse=True)

numbers = input().split()
numbers_as_digits = []
for number in numbers:
    numbers_as_digits.append(int(number))

sorted_numbers = sorting_numbers(numbers_as_digits)
print(sorted_numbers)



#############################################
print(sorted(sorted_numbers, reverse=True))
print(sorted(["Pesho", 'neshto si tam', "Abrakadavra"]))
