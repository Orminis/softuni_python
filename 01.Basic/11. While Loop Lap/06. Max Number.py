import sys

command = input() #цяло число или стоп


max = -sys.maxsize

while command != "Stop":
    number = int(command)   # преобразуваме текста в число
    # проверка дали е най-голямо число
    if number > max:
        max = number

    command = input()
print(max)
