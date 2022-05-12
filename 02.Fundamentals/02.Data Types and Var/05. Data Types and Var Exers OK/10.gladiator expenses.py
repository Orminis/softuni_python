# How much will cost the repair of his gladiator's equipment
# Helmet, a sword, a shield and an armor
#every second lost fight helmet's broken
#every third lost fight the sword is broken
#if both helmet and sword are broken, also the shield is broken
#every 2nd time his shield is broken also the armor breaks.
#calculate the price for repairs. first number will be integer with lost fights

lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())


helmet_cost = (lost_fights // 2) * helmet_price
sword_cost = (lost_fights // 3) * sword_price
shield_cost = (lost_fights // 6) * shield_price
armor_cost = (lost_fights // 12) * armor_price
total_expenses = helmet_cost + shield_cost + sword_cost + armor_cost
print(f"Gladiator expenses: {total_expenses:.2f} aureus.")
