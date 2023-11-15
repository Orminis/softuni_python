"""
Explosions are marked with '>'. Immediately after the mark, there will be an integer x,
which signifies the strength of the explosion.
You should remove x characters, starting after the punch character ('>').
If you find another explosion mark ('>') while you are deleting characters,
you should add the strength to your previous explosion.
You should not delete the explosion character – '>'.
When all characters are processed, print the final string.
"""
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