"""
Write a program which reads N lines of strings and extracts the name and the age of a given person.
The name of the person  be between '@' and '|'. The person’s age will be between '#' and '*'.

Example:
    "Hello my name is @Peter| and I am #20* years old."

For each found name and age print a line in the following format
    "{name} is {age} years old.".
"""

def check_symbol(symbol):
    if symbol == "@":
        return "@"
    elif symbol == "#":
        return "#"


def take_name_and_age(string_to_be_checked):
    for idx, ch in enumerate(string_to_be_checked):
        if ch == "|":
            return string_to_be_checked[:idx:]
        if ch == "*":
            return string_to_be_checked[:idx:]


nums_of_lines = int(input())
spec_symbols = {"@", "#",}

for ln in range(nums_of_lines):
    name = ''
    age = ''

    str_to_be_checked = input()

    for indx, ch in enumerate(str_to_be_checked):
        symbol = ''
        if ch in spec_symbols:
            symbol = check_symbol(ch)

            if symbol == "@":
                name = take_name_and_age(str_to_be_checked[indx+1::])
            elif symbol == "#":
                age = take_name_and_age(str_to_be_checked[indx+1::])

    print(f"{name} is {age} years old.")
