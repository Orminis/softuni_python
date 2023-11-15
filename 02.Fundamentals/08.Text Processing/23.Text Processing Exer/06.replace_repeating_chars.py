"""
Write a program which reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.
"""
data = input()

index = 0
while index < len(data) - 1:
    if data[index] == data[index + 1]:
        element_to_replace = f"{data[index]}{data[index + 1]}"
        data = data.replace(element_to_replace, data[index])
        if index == 0:
            pass
        else:
            index -= 1
    else:
        index += 1
print(data)


##############################################################
data = input()

index = 0
while index < len(data) - 1:
    if data[index] == data[index + 1]:
        element_to_replace = f"{data[index]}{data[index + 1]}"
        data = data.replace(element_to_replace, data[index])
        index = 0
    else:
        index += 1
print(data)