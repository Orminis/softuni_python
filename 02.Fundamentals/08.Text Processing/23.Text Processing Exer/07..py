content = input()

index = 0
result = ""
current_explosion = 0

while index < len(content):
    if content[index] == ">":
        result += content[index]
        index += 1
        current_explosion += int(content[index])
        current_explosion -= 1
    else:
        if current_explosion > 0:
            current_explosion -= 1
        else:
            result += content[index]
    index += 1

print(result)