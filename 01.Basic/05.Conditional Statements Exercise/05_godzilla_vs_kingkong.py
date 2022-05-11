budget = float(input())
number_of_actors = int(input())
price_for_dresses = float(input())

decor = budget * 0.10
total_price_for_dresses = number_of_actors * price_for_dresses

if number_of_actors > 150:
    total_price_for_dresses -= total_price_for_dresses * 0.10

total_cost = decor + total_price_for_dresses

if total_cost > budget:
    needed_money = total_cost - budget
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
else:
    left_money = budget - total_cost
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")