price_for_vegies = float(input())
price_for_fruits = float(input())
kg_of_vegies = int(input())
kg_of_fruits = int(input())

total_sum = (price_for_vegies * kg_of_vegies) + (price_for_fruits * kg_of_fruits)
total_sum = total_sum / 1.94
print(f"{total_sum:.2f}")
