rent_for_hall = int(input())

price_for_cake = rent_for_hall * 0.2
price_for_drinks = price_for_cake - (price_for_cake * 45 / 100)
animator = rent_for_hall / 3
total_amount = rent_for_hall + price_for_cake + price_for_drinks + animator
print(total_amount)