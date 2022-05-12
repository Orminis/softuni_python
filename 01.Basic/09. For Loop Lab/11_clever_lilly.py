age_of_lilly = int(input())
price_for_laundry_machine = float(input())
toy_price = int(input())

saved_money = 0
# Пари от рожденни дни
for birthday in range(1, age_of_lilly + 1):
    if birthday % 2 == 0:
        saved_money += (birthday * 10 / 2) - 1 #money
    else:
        saved_money += toy_price #toys

diff = abs(saved_money - price_for_laundry_machine)
if saved_money >= price_for_laundry_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
