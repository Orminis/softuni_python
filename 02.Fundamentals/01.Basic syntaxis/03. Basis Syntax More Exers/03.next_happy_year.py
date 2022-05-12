# Lets find next Happy new year (year in which each digit is different)

# First - with set function

# current_year = input()
#
# while True:
#     current_year += 1
#     current_year_as_string = str(current_year)
#     if len(current_year_as_string) == len(set(current_year_as_string)):  #set function in len returns only
#                                                                           for unique items in the len
#         print(current_year_as_string)
#         break

# Second way - with nested conditions

current_year = int(input())
while True:
    current_year += 1
    current_year_as_string = str(current_year)
    happy_year = True
    for i in range(len(current_year_as_string)):
        y = current_year_as_string[i]
        for x in range(i + 1, len(current_year_as_string)):
            if y == current_year_as_string[x]:
                happy_year = False
                break
    if happy_year:
        print(current_year)
        break
