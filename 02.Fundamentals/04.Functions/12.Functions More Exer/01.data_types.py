"""Write a function that, depending on the first line of the input, reads one of the following strings:
"int","real", or"string".
If the data type is an int, multiply the number by 2.
If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
If the data type is a string, surround the input with "$".
Print the result on the console.
"""


def data_type(data):
    if data == "int":
        int_num = int(input())
        result = int_num * 2
        return print(result)
    elif data == "real":
        fl_num = float(input())
        result = fl_num * 1.5
        return print(f"{result:.2f}")
    elif data == "string":
        str = input()
        return print(f"${str}$")


data = input()
data_type(data)
