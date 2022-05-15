import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
txt = input()
matches = re.finditer(pattern, txt)

for match in matches:
    print(match.group(0), end=" ")
