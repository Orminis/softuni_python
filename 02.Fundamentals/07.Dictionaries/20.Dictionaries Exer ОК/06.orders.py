# command = input()
#
# product_dict = {}
#
# while not command == "buy":
#     name, price, quantity = command.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if name not in product_dict:
#         product_dict[name] = [price, quantity]
#     else:
#         product_dict[name][0] = price
#         product_dict[name][1] += quantity
#
#     command = input()
#
# for name in product_dict:
#     total_price = product_dict[name][0] * product_dict[name][1]
#     print(f"{name} -> {total_price:.2f}")

command = input()

product_dict = {}
second_dict = {}

while not command == "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in product_dict:
        product_dict[name] = price
        second_dict[name] = quantity
    else:
        product_dict[name] = price
        second_dict[name] += quantity

    command = input()

for name in product_dict:
    total_price = product_dict[name] * second_dict[name]
    print(f"{name} -> {total_price:.2f}")