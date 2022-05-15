import re

command = input()
furn_list = []
total_sum = 0.00
while not command == "Purchase":
    pattern = r"^>>([A-Za-z]+)<<([0-9]+[0-9\.]+)!(\d+)$"
    match = re.search(pattern, command)

    if match:
        furniture, price, quantity = match.groups()
        furn_list.append(furniture)
        total_sum += float(price) * int(quantity)

    command = input()

print(f"Bought furniture:")

if len(furn_list) > 0:
    print("\n".join(furn_list))

print(f"Total money spend: {total_sum:.2f}")
