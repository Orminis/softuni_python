data = input().split()
products = {}

for index in range(0, len(data), 2):
    current_product = data[index]
    quantity = int(data[index + 1])
    products[current_product] = quantity

searched_products = input().split()

for s_product in searched_products:
    if s_product not in products:           #searches through keys in products dictionary
        print(f"Sorry, we don't have {s_product}")
    else:
        print(f"We have {products[s_product]} of {s_product} left")
