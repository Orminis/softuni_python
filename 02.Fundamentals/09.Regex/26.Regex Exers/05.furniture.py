"""
Write a program which calculates the total cost of bought furniture.
You will be given information about each purchase on separate lines until you receive the command "Purchase".
Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}".
The price could be floating-point or integer number. You should store the names of the furniture and the total price.
At the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
    "Bought furniture:
    {1st name}
    {2nd name}
    …
    {N name}
    Total money spend: {total_cost}"

Example input:
>>Sofa<<312.23!3
>>TV<<300!5
>Invalid<<!5
Purchase
Output:
Bought furniture:
Sofa
TV
Total money spend: 2436.69
"""
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
