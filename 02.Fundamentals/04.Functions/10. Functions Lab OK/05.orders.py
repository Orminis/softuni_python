#single product and the price for its order

def order_price(product, quantity):
    if product == "coffee":
        price = 1.50 * quantity
    elif product == "water":
        price = 1.00 * quantity
    elif product == "coke":
        price = 1.40 * quantity
    elif product == "snacks":
        price = 2.00 * quantity

    return(price)


product = input()
quantity = float(input())
order = order_price(product, quantity)
print(f"{order:.2f}")
