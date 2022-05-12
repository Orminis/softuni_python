n1 = int(input())
n2 = int(input())
operator = input()

if operator == "+":
    sum = n1 + n2
    if sum % 2 == 0:
        a = "even"
    else:
        a = "odd"
elif operator == "-":
    sum = n1 - n2
    if sum % 2 == 0:
        a = "even"
    else:
        a = "odd"

elif operator == "*":
    sum = n1 * n2
    if sum % 2 == 0:
        a = "even"
    else:
        a = "odd"

elif operator == "/":
    if n2 != 0:
        sum = n1 / n2
        print(f"{n1} / {n2} = {sum:.2f}")

    elif n2 == 0:
        print(f"Cannot divide {n1} by zero")
elif operator == "%":
    if n2 != 0:
        sum = n1 % n2
        print(f'{n1} % {n2} = {sum}')
    elif n2 == 0:
        print(f"Cannot divide {n1} by zero")

if operator in "+" "-" "*":
    print(f'{n1} {operator} {n2} = {sum} - {a}')
