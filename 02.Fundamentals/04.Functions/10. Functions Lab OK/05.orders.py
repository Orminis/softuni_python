#single product and the price for its order

def order_price(prod, quant):
    if prod == "coffee":
        price = 1.50 * quant
    elif prod == "water":
        price = 1.00 * quant
    elif prod == "coke":
        price = 1.40 * quant
    elif prod == "snacks":
        price = 2.00 * quant

    return price


product = input()
quantity = float(input())
order = order_price(product, quantity)
print(f"{order:.2f}")
