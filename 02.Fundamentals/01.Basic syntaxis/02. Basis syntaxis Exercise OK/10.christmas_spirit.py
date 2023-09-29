# Christmas Spirit
"""
You will receive an allowed quantity for one type of decoration and days left until Christmas day to decorate the house.
There are 4 types of decorations, and each piece costs a price
Ornament Set – 2$ per piece
Tree Skirt – 5$ per piece
Tree Garlands – 3$ per piece
Tree Lights – 15$ per piece
Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.
Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.
Every fifth day you buy Tree Lights and increase your Christmas spirit by 17. If you have bought
 Skirts and Tree Garlands on the same day, you additionally increase your spirit by 30.
Every tenth day you lose 20 points of the spirit because your cat ruins all tree decorations,
and you should rebuild the tree and buy one piece of tree skirt, garlands, and lights.
That is why you are forced to increase the allowed quantity with 2 at the beginning of every eleventh day.
Also, if the last day is a tenth day, the cat demolishes even more and ruins the Christmas turkey,
 you lose an additional 30 points of spirit.
It the end, you must print the total cost and the gained spirit.
"""

quantity = int(input())
remaining_days = int(input())

budget = 0
total_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        budget += ornament_set_price * quantity
        total_spirit += 5
    if current_day % 3 == 0:
        budget += tree_skirt_price * quantity
        budget += tree_garland_price * quantity
        total_spirit += 13
    if current_day % 5 == 0:
        budget += tree_lights_price * quantity
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        budget += tree_skirt_price + tree_garland_price + tree_lights_price

if remaining_days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")