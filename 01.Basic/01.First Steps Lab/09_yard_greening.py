# Calculate how much will cost greening of a yard

square_meters = float(input())
price = square_meters * 7.61
discount = 0.18 * price
final_price = price - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")