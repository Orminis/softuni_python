number_of_days = int(input())
type_of_room = input()
rating = input()
costs = 0

if type_of_room == 'room for one person':
    costs = (number_of_days - 1) * 18

elif type_of_room == 'apartment':
    costs = (number_of_days - 1) * 25
    if number_of_days < 10:
        costs -= costs * 0.30
    elif 10 <= number_of_days <= 15:
        costs -= costs * 0.35
    elif number_of_days > 15:
        costs -= costs * 0.50

elif type_of_room == 'president apartment':
    costs = (number_of_days - 1) * 35
    if number_of_days < 10:
        costs -= costs * 0.10
    elif 10 <= number_of_days <= 15:
        costs -= costs * 0.15
    elif number_of_days > 15:
        costs -= costs * 0.20

if rating == 'positive':
    costs += costs * 0.25
else:
    costs -= costs * 0.10

print(f'{costs:.2f}')