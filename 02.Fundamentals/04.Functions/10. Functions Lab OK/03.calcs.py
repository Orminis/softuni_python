#to create a function that receives parameters and calculates
#multiply divide add substract

def calculate(operator, number_one, number_two):

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    res = 0
    if operator == "multiply":
        res = multiply(number_one, number_two)
    elif operator == "divide":
        res = divide(number_one, number_two)
    elif operator == "add":
        res = add(number_one, number_two)
    elif operator == "subtract":
        res = subtract(number_one, number_two)

    return res


operator = input("Choose from multiply, divide, add or subtract")
first_num = int(input())
second_num = int(input())
result = int(calculate(operator, first_num, second_num))
print(result)


