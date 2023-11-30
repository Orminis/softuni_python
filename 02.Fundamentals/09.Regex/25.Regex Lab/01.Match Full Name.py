"""Write a program to match full names from a sequence of characters and print them on the console.

First, write a regular expression to match a valid full name, according to these conditions:
A valid full name has the following characteristics:
    oIt consists of two words.
    oEach word starts with a capital letter.
    oAfter the first letter, it only contains lowercase letters afterwards.
    oEach of the two words should be at least two letters long.
    oThe two words are separated by a single space.
"""
import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
names = input().split(", ")

valid_names = []

for name in names:
    match = re.match(pattern, name)
    if match:
        valid_names.append(match.group())

print(" ".join(valid_names))

################################################

import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
names = input()

valid_names = re.findall(pattern, names)
print(" ".join(valid_names))