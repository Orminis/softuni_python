"""
Write a program which finds all integer and floating-point numbers in a string.
Compose the Regular Expression
A number has the following characteristics:
    Has either whitespace before it or the start of the string (match either ^ or what's called a positive lookbehind).
        The entire syntax for the beginning of your RegEx might look something like "(^|(?<=\s))".
    The number might or might not be negative, so it might have a hyphen on its left side ("-").
    Consists of one or more digits.
    Might or might not have digits after the decimal point
    The decimal part (if it exists) consists of a period (".") and one or more digits after it. Use a capturing group.
    Has either whitespace before it or the end of the string (match either $ or what's called a positive lookahead).
        The syntax for the end of the RegEx might look something like "($|(?=\s))".
Example input:
1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5
Output:
1 -1 123 -123 123.456 -123.456
"""
import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
txt = input()
matches = re.finditer(pattern, txt)

for match in matches:
    print(match.group(0), end=" ")

# Another way to iterate through the found matches from the finditter() function.
# valid_nums = [num.group() for num in matches]
# print(*valid_nums)