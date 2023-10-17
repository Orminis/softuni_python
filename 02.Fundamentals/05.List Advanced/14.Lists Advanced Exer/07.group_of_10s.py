"""
Write a program that receives a sequence of numbers (a string containing integers separated by ", ")
and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
Examples:
The numbers 2, 8, 4, and 10 fall into the group of 10's.
The numbers 13, 19, 14, and 15 fall into the group of 20's.
"""

list_of_numbers = [int(x) for x in input().split(", ")]
group = 10
while list_of_numbers:
    group_list = []

    for x in list_of_numbers:
        if x in range(group-10, group+1):
            group_list.append(x)

    for x in group_list:
        list_of_numbers.remove(x)

    print(f"Group of {group}'s: {list(group_list)}")
    group += 10


# ##########################################################

list_of_numbers = [int(x) for x in input().split(", ")]
group_list = []
counter = 1
while True:
    for x in range(1, len(list_of_numbers)):
        group = counter * 10
        for i in list_of_numbers[::-1]:
            if i <= group:
                group_list.append(list_of_numbers.pop(list_of_numbers.index(i)))
        counter += 1
        print(f"Group of {group}'s: {list(reversed(group_list))}")
        group_list = []
        if len(list_of_numbers) == 0:
            break
    break
