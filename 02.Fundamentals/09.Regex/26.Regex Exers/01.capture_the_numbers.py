"""
Write a program which receives series of strings on different lines and extracts only the numbers.
Print all extracted numbers on a single line, separated by a single space.

Example input:
The300
What is that?
I think it's the 3rd movie
Let's watch it at 22:45
Output:
300 3 22 45
"""
import re

pattern = r"\d+"
line = input()
while line:
    match = re.findall(pattern, line)
    if match:
        print(' '.join(match), end=' ')
    line = input()

