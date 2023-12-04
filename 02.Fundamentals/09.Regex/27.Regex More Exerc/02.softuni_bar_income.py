"""
Let`s take a break and visit the game bar at SoftUni. It is about time for the people behind the bar to go home and you are the person who has to draw the line and calculate the money from the products that were sold throughout the day.
Until you receive a line with text "end of shift" you will be given lines of input.
But before processing that line you should do some validations first.
Each valid order should have a customer, product, count and a price:
    Valid customer's name should be surrounded by '%' and must start with a capital letter, followed by lower-case letters
    Valid product contains any word character (not only letters) and must be surrounded by '<' and '>'
    Valid count is an integer, surrounded by '|'
    Valid price is any real number followed by '$'
The parts of a valid order should appear in the order given: customer, product, count and a price.
Between each part there can be other symbols, except ('|', '$', '%' and '.')
For each valid line print on the console: "{customerName}: {product} - {totalPrice}"
When you receive "end of shift" print the total amount of money for the day rounded to 2 decimal places in the following format: "Total income: {income}".
Input / Constraints
Strings that you have to process until you receive text "end of shift".
Output
    Print all of the valid lines in the format "{customerName}: {product} - {totalPrice}"
    After receiving "end of shift" print the total amount of money for the day rounded to 2 decimal places in the following format: "Total income: {income}"
Example Input:
%George%23<Croissant>|2|10.3$
%Peter%1<Gum>|1|1.3$
%Maria%sda<Cola>|1|2.4$
end of shift
Output:
George: Croissant - 20.60
Peter: Gum - 1.30
Maria: Cola - 2.40
Total income: 24.30
"""

import re

pattern = r"%(?P<name>[A-Z]{1}[a-z]+)%" \
          r"[^|$%.]*" \
          r"<(?P<product>[\w]+)>" \
          r"[^|$%.]*" \
          r"\|(?P<count>[\d]+)\|"\
          r"[^|$%.\d]*" \
          r"(?P<price>[\d]+\.?[\d]*)\$"

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
print(f"Total income: {total_income:.2f}")

