price_vacation = float(input())
puzzle = int(input())
talking_dolls = int(input())
fluffy_bears = int(input())
minions = int(input())
truck = int(input())

toys_count = puzzle + talking_dolls + fluffy_bears + minions + truck

toys_price = puzzle * 2.60 + talking_dolls * 3 + fluffy_bears * 4.10 + minions * 8.20 + truck * 2

if toys_count >= 50:
    toys_price = toys_price - (toys_price * 0.25)

rent = toys_price * 0.1
final_price = toys_price - rent
profit = abs(final_price - price_vacation)

if final_price >= price_vacation:
    print(f"Yes! {profit:.2f} lv left.")

else:
    print(f"Not enough money! {profit:.2f} lv needed.")