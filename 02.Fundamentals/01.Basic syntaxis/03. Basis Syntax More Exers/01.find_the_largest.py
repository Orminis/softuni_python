number = str(input())

sorted_list = sorted(number, reverse=True)
list_to_number = ''
for i in sorted_list:
    list_to_number += i

print(list_to_number)

list_to_number = [i for i in sorted_list]
print(f"{i}" for i in list_to_number)