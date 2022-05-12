budget = float(input())         #available budget money
flour_price = float(input())    #price per 1kg of flour

#recipe for the easter bread
#1 pack of eggs, 1kg of flour, 250ml of milk
#We are looking how much bread we can make with our budget (always remain some of the budget)

eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4                   #Price per 250ml of milk
price_per_bread = eggs_price + flour_price + milk_price

bread_counter = 0
colored_eggs = 0

while budget >= 0:
    if budget - price_per_bread > 0:
        bread_counter += 1
        colored_eggs += 3
        budget -= price_per_bread
        if bread_counter % 3 == 0:
            colored_eggs -= (bread_counter - 2)
    else:
        break
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

