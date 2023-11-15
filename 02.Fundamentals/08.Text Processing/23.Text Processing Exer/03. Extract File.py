"""Write a program which reads the path to a file and subtracts the file name and its extension."""

path = input().split(f"{chr(92)}")
divide_string = path[-1]
name, extension = divide_string.split(".")
print(f"File name: {name}\nFile extension: {extension}")
