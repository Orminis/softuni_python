from math import floor, ceil

days_alone = int(input())
left_food = int(input())
dog_food_per_day_in_kg = float(input())
cat_food_per_day_in_kg = float(input())
turtle_food_per_day_in_grams = float(input())

needed_dog_food = days_alone * dog_food_per_day_in_kg
needed_cat_food = days_alone * cat_food_per_day_in_kg
needed_turtle_food = days_alone * turtle_food_per_day_in_grams / 1000

total_needed_food = needed_dog_food + needed_cat_food + needed_turtle_food

if left_food >= total_needed_food:
    food = floor(left_food - total_needed_food)
    print(f"{food} kilos of food left.")
else:
    food = ceil(total_needed_food - left_food)
    print(f"{food} more kilos of food are needed.")