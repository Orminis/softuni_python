import sys

command = input() #цяло число или стоп
min = sys.maxsize

while command != "Stop":
    number = int(command)   # преобразуваме текста в число

    if number < min:        # проверка дали е най-malkoto число
        min = number

    command = input()       # Въвеждаме следващото число

print(min)
