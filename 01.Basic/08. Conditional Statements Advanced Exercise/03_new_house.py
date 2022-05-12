type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())

if type_of_flowers == 'Roses':
    price_of_flowers = 5 * number_of_flowers
    if number_of_flowers > 80:
        price_of_flowers -= price_of_flowers * 0.10

elif type_of_flowers == 'Dahlias':
    price_of_flowers = 3.80 * number_of_flowers
    if number_of_flowers > 90:
        price_of_flowers -= price_of_flowers * 0.15


elif type_of_flowers == 'Tulips':
    price_of_flowers = 2.80 * number_of_flowers
    if number_of_flowers > 80:
        price_of_flowers -= price_of_flowers * 0.15


elif type_of_flowers == 'Narcissus':
    price_of_flowers = 3 * number_of_flowers
    if number_of_flowers < 120:
        price_of_flowers += price_of_flowers * 0.15


elif type_of_flowers == 'Gladiolus':
    price_of_flowers = 2.50 * number_of_flowers
    if number_of_flowers < 80:
        price_of_flowers += price_of_flowers * 0.20

if budget >= price_of_flowers:
    left_money = budget - price_of_flowers
    print(f'Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {left_money:.2f} leva left.')

else:
    needed_money = price_of_flowers - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")
