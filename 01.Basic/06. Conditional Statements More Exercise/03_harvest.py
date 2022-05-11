import math

area_of_vineyard = int(input())
grapes_per_sq_m = float(input())
needed_wine_in_l = int(input())
workers = int(input())

wine = area_of_vineyard * grapes_per_sq_m * 0.4 / 2.5
left_wine = wine - needed_wine_in_l
not_enough_wine = needed_wine_in_l - wine
wine_per_person = left_wine / workers

if wine >= needed_wine_in_l:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(left_wine)} liters left -> {math.ceil(wine_per_person)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(not_enough_wine)} liters wine needed.")
