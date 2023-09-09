# Calculate price of the fruits from the local market.

strawberry_price = float(input())
bananas = float(input())
oranges = float(input())
raspberry = float(input())
strawberry = float(input())

#price of products
raspberry_price = strawberry_price / 2
oranges_price = raspberry_price * 0.6
bananas_price = raspberry_price * 0.2

# sum per kind of fruit
sum_for_raspberries = raspberry * raspberry_price
sum_for_oranges = oranges * oranges_price
sum_for_bananas = bananas * bananas_price
sum_for_strawberry = strawberry * strawberry_price

# Total amount of money for all fruits
total_sum = sum_for_strawberry + sum_for_bananas + sum_for_oranges + sum_for_raspberries
print(total_sum)