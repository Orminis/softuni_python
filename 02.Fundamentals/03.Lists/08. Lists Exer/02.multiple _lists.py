factor = int(input())
count = int(input())

list_of_numbers = []
# for multiplier in range(1, count +1):
#     list_of_numbers.append(factor * multiplier)

for num in range(count):
    list_of_numbers.append(factor + num * factor)
    list_of_numbers.sort()
print(list_of_numbers)
