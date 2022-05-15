data = input().split()

products = {}

for index in range(0, len(data), 2):
    current_product = data[index]
    quantity = data[index + 1]
    products[current_product] = int(quantity)

print(products)


# products = {i for i in range(0,len(data), 2)}
# print(products)
