path = input().split(f"{chr(92)}")
divide_string = path[-1]
name, extension = divide_string.split(".")
print(f"File name: {name}\nFile extension: {extension}")
