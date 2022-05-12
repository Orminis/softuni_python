## Invert the numbers in the list

##First way

# list_of_numbers = input().split()
#
# opposite_numbers = []    #list() other
#
# for index in range(len(list_of_numbers)):
#     opposite_number = -int(list_of_numbers[index])
#     opposite_numbers.append(opposite_number)
# print(opposite_numbers)




### Second with list comprehensions ###
# list_of_numbers = input().split()
# opposite_numbers = [-int(s) for s in list_of_numbers]
# print(opposite_numbers)


