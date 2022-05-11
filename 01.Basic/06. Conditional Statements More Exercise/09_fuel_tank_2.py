fuel_type = input()
fuel_quantity = float(input())
club_card = input()
price = float()

gasoline = 2.22  # Цена за литър бензин
diesel = 2.33  # Цена на литър дизел
gas = 0.93  # Цената на литър газ

if club_card == 'Yes' and fuel_type == 'Gas':
    if fuel_quantity > 25:
        price = 0.9 * (0.85 * fuel_quantity)
    elif 20 <= fuel_quantity <= 25:
        price = 0.92 * (0.85 * fuel_quantity)
    else:
        price = 0.85 * fuel_quantity
elif club_card == 'No' and fuel_type == 'Gas':
    if fuel_quantity > 25:
        price = 0.9 * (0.93 * fuel_quantity)
    elif 20 <= fuel_quantity <= 25:
        price = 0.92 * (0.93 * fuel_quantity)
    else:
        price = 0.93 * fuel_quantity

if club_card == 'Yes' and fuel_type == 'Gasoline':
    if fuel_quantity > 25:
        price = 0.9 * (2.04 * fuel_quantity)
    elif 20 <= fuel_quantity <= 25:
        price = 0.92 * (2.04 * fuel_quantity)
    else:
        price = 2.04 * fuel_quantity
elif club_card == 'No' and fuel_type == 'Gasoline':
    if fuel_quantity > 25:
        price = 0.9 * (2.22 * fuel_quantity)
    elif 20 <= fuel_quantity <= 25:
        price = 0.92 * (2.22 * fuel_quantity)
    else:
        price = 2.22 * fuel_quantity

if club_card == 'Yes' and fuel_type == 'Diesel':
    if fuel_quantity > 25:
        price = 0.9 * (2.21 * fuel_quantity)
    elif 20 <= fuel_quantity <= 25:
        price = 0.92 * (2.21 * fuel_quantity)
    else:
        price = 2.21 * fuel_quantity
elif club_card == 'No' and fuel_type == 'Diesel':
    if fuel_quantity > 25:
        price = 0.9 * (2.33 * fuel_quantity)
    elif 20 <= fuel_quantity <= 25:
        price = 0.92 * (2.33 * fuel_quantity)
    else:
        price = 2.33 * fuel_quantity
print(f'{price:.2f} lv.')