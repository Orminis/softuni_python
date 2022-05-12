def factorial(number):
    for index in range(1, number):
        number *= index
    return number


first_number = int(input())
second_number = int(input())
result = factorial(first_number) / factorial(second_number)
print(f"{result:.2f}")
