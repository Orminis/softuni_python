import re

some_input = input()

pattern = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(pattern, some_input)
print(", ".join(matches))