list_of_integers = [int(x) for x in input().split()]
numbers_for_removal = int(input())

lowest_numbers = sorted(list_of_integers)[:numbers_for_removal]
[list_of_integers.remove(char) for char in list_of_integers if char in lowest_numbers]
# for char in list_of_integers:
#     if char in lowest_numbers:
#         list_of_integers.remove(char)

print(f"{', '.join([str(x) for x in list_of_integers])}")
