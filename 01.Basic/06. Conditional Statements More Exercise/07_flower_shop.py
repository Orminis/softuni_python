from math import ceil, floor

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

magnolias_price = 3.25
hyacinths_price = 4.00
roses_price = 3.50
cacti_price = 8.00

total_price = magnolias * magnolias_price + hyacinths * hyacinths_price + roses * roses_price + cacti * cacti_price

final_profit = total_price - (total_price * 0.05)

left_money = floor(final_profit - gift_price)
money_to_borrow = ceil(gift_price - final_profit)

if left_money >= 0:
    print(f"She is left with {left_money} leva.")
else:
    print(f"She will have to borrow {money_to_borrow} leva.")