import re

pattern = r"%(?P<name>[A-Z][a-z]+)%[^|$%.]*<(?P<product>[A-Za-z0-9]+)>[^|$%.]*\|(?P<count>[\d]+)\|[^|$%.\d+]*(?P<price>[\d]+\.?[\d]+)\$"

total_income = 0

command = input()

while not command == "end of shift":
    valid_order = re.search(pattern, command)
    if valid_order is not None:
        name = valid_order.group("name")
        product = valid_order.group("product")
        total_price = int(valid_order.group("count")) * float(valid_order.group("price"))
        total_income += total_price
        print(f"{name}: {product} - {total_price:.2f}")

    command = input()
print(f"Total income: {total_income:2f}")

